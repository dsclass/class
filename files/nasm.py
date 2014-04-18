#!/usr/bin/env python
import os
import subprocess
import sys
import tempfile

PROMPT = "asm (%d)# "
FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])

END_PROG_LIST = ("quit", "exit")
END_SEQ_LIST  = ("end", "endloop", "done")

class Nasm:
    #nasm_custom = "/home/doug/tools/nasm-2.01/nasm"
    nasm_custom_opts = "-O9 -f elf -o %s.bin"
    #ndis_custom = "/usr/bin/objdump"
    ndis_custom_opts = "-d"

    nasm_list = ('nasm', 'nasm.exe', 'nasmw.exe')
    nasm_opts = "-O9 -f bin -o %s.bin"
    ndis_list = ('ndisasm', 'ndisasm.exe', 'ndisasmw.exe')
    ndis_opts = "-b 32"

    def __init__(self):
        self.fVerbose = False
        self.nasm = ""
        self.ndisasm = ""

        if not self.check():
            raise EnvironmentError('nasm and/or ndisasm not found.')
        self.clear()

    def add(self, asm):
        if asm.strip():
            self.buffer.append(asm)

    def clear(self):
        self.buffer = ["BITS 32"]
        self.bin = ""
        self.disasm = ""

    def verbose(self, flag=True):
        self.fVerbose = flag

    def count(self):
        return len(self.buffer)

    def check(self):
        found_nasm = False
        found_ndis = False
        paths = os.environ['PATH'].split(':')

        for path in paths: 
            for nasm in self.nasm_list:
                if os.path.exists(os.path.join(path, nasm)):
                    self.nasm = os.path.join(path, nasm)
            for ndisasm in self.ndis_list:
                if os.path.exists(os.path.join(path, ndisasm)):
                    self.ndisasm = os.path.join(path, ndisasm)

        try:
            if os.path.exists(self.nasm_custom):
                self.nasm      = self.nasm_custom 
                self.nasm_opts = self.nasm_custom_opts

            if os.path.exists(self.ndis_custom):
                self.ndisasm   = self.ndis_custom
                self.ndis_opts = self.ndis_custom_opts
        except AttributeError:
            pass

        if self.nasm and self.ndisasm:
            return True
        else:
            return False


    def assemble(self):
        if self.fVerbose:
            print "----| Assembling" 
            print "\n".join(self.buffer)
            print "\n"

        (fd, tmpname) = tempfile.mkstemp(prefix="nasmtmp-")
        os.write(fd, "\n".join(self.buffer))
        os.close(fd)
        
        cmd = [self.nasm,
               self.nasm_opts % tmpname,
               tmpname]

        try:
            ret = subprocess.call(" ".join(cmd), shell=True)
            if ret != 0:
                raise OSError("nasm failed")
        except OSError, e:
            print >>sys.stderr, "Error:", e
            bin = ""
        else:
            bin = open(tmpname + ".bin", "rb").read()

        try:
            os.remove(tmpname)
            os.remove(tmpname + ".bin")
        except:
            pass

        self.bin = bin

    def disassemble(self):
        (fd, tmpname) = tempfile.mkstemp(prefix="nasmtmp-")
        os.write(fd, self.bin)
        os.close(fd)

        cmd = [self.ndisasm,
               self.ndis_opts,
               tmpname]
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            if proc.wait() != 0:
                raise OSError("nasm failed")
        except OSError, e:
            print >>sys.stderr, "Error:", e
            disasm = ""
        else:
            disasm = proc.stdout.read()

        try:
            os.remove(tmpname)
        except:
            pass

        self.disasm = disasm

        print "----| Diassembly"
        print self.disasm

    def hexdump(self, src=None, length=16):
        if not self.fVerbose:
            return 

        print "----| Hex Dump"
        i = 0
        totalBytes = 0
        if src == None:
            src = self.bin
        while src:
            line, src = src[:length], src[length:]
            hexa = ' '.join(["%02X" % ord(x) for x in line])
            totalBytes += len(line)
            line = line.translate(FILTER)
            print "%04X:  %-*s   %s" % (i, length*3, hexa, line)
            i += length
        print "Size: 0x%x (%d) bytes" % (totalBytes, totalBytes)
        print "\n"

def main():
    try:
        nasm = Nasm()
    except EnvironmentError, e:
        print "Error:", e
        sys.exit(-1)

    nasm.verbose()
    while 1:
        try:
            try:
                cmd = raw_input(PROMPT % nasm.count())
            except EOFError:
                cmd = 'done'

            if cmd.lower() in END_PROG_LIST:
                raise EOFError
            elif cmd.lower() in END_SEQ_LIST:
                sys.stdout.write("\n")
                nasm.assemble()
                nasm.hexdump()
                nasm.disassemble()
                nasm.clear()
            else:
                nasm.add(cmd)
        except (EOFError, KeyboardInterrupt):
            print "\nExiting"
            break


if __name__ == "__main__":
    main()


