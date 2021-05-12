<h1 align="center">CTF Write-Ups</h1>
<h6 align="center"><i>My CTF journey since 2020</i></h6>

## Upcoming CTFs
| CTF | Period | 
| :-: | :----: |
| Plaid CTF | April |
| Midnight Sun CTF | April |
| DEFCON CTF | May |
| 0CTF | June |
| HSCTF | June |
| Google CTF | ~August |
| ⭐ Flare-On CTF | ~September |
| DownUnder CTF | ~September |
| ALLES! CTF | ~September |
| Hitcon CTF | October-November |
| Dragon CTF | November |
| ⭐ X-MAS CTF | December |


## Tools used
**Set up:**
* Flare VM
* Kali linux

| Category | Sub Category | Tool | Description |
| :------- | :----------- | :--- | :---------- |
| **Reverse Engineering** | Tool kit | Remnux | VM with most of the malware analysis tools
|                         | Tool kit | Flare | VM with most of the malwre analysis tools
|                         | Code Analysis | ⭐ ida pro | Decompiler
|                         | Code Analysis | Ghidra | Decompiler
|                         | Code Analysis | x64dbg | Debugger
|                         | Static Analysis | ⭐ [Code Beautifier](https://beautifier.io/) | Add indents and stuff to obfuscated code
|                         | Executables | [Binary Ninja](https://cloud.binary.ninja/) | Binary analysis in the cloud
|                         | Executables | ⭐ [angr](https://github.com/angr/angr) | Binary analysis framework
|                         | Executables | [dll_to_exe](https://github.com/hasherezade/dll_to_exe) | convert dlls to executables to pop into ida
|                         | Mobile | [apk tool](https://ibotpeaches.github.io/Apktool/) | Android apk decompiler (working with smali files)
|                         | Mobile | ⭐ [jd-gui online](http://www.javadecompilers.com/apk) | Android apk decompiler (Personal favourite)
|                         | Mobile | ⭐ [dex2jar]() | Extract the apk file, d2j-dex2jar app.apk (kali)
| **Forensics** | Executables | ⭐ Detect it easy | Determine file type (Windows)
|               | Executables | file | Determine file type (Linux command)
|               | Shellcode Analysis | [scDbg](http://sandsprite.com/blogs/index.php?uid=7&pid=152) | Analyse shellcode
|               | Network | ⭐ Wireshark | Network packets analyzer
|               | Network | ⭐ Fiddler/ Burp | Network interceptor
|               | Web | [SpiderMonkey](https://spidermonkey.dev/) | Javascript interpreter 
|               | Web | [cscripts](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cscript) | Run javascript code in the commandline
|               | Web | [V8](https://v8.dev/) | Javascript engine 
|               | binwalk | Analyse hidden files
|               | PDF | Foxit Reader | For dynamically analyzing pdf files, and looking at the behaviour of the pdf
|               | PDF | [pdfid.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pdfid.py) | To view the pdf structure and other static analysis
|               | PDF | [pdf-parser.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pdf-parser.py) | To examine pdf objects
|               | PDF | [peepdf.py](https://github.com/jesparza/peepdf) | To analyse the pdf file
|               | Office | ⭐ [olevba](https://github.com/decalage2/oletools/tree/master/oletools) | Extract macros from office files
|               | Office | ⭐ pcodedmp | For analysing office files that are vba stomped
|               | Zip files | [pkcrack](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html) | Cracking zip files
|               | Memory | [volatility](https://github.com/volatilityfoundation/volatility) | Memory Analysis
| **Miscellaneous** |  | ⭐ [stegseek](https://github.com/RickdeJager/stegseek) | Steghide cracker
|                   |  | ⭐ [zsteg](https://github.com/zed-0xff/zsteg) | `zsteg -a` Hail mary on stego file
|                   |  | ⭐ [z3](https://github.com/Z3Prover/z3) | Theorem prover
|                   |  | ⭐ [pytesseract](https://pypi.org/project/pytesseract/) | Python wrapper for google tesseract OCR engine 
| **OSINT** |  | ⭐ [sherlock](https://github.com/sherlock-project/sherlock) | finding social media handles
|           |  | ⭐ [wayback machine](https://archive.org/web/) | Finding deleted tweets and stuff
| **Binary Exploitation** |  | ⭐ [pwntools](https://github.com/Gallopsled/pwntools) | Scripting
|                         |  | gdb | debugging stuff
| **Web** |  | sqlmap    | SQL injection 
|         |  | dirbuster | Enumerate Directories
|         |  | [jwt_tool](https://github.com/ticarpi/jwt_tool) | forging jwt 
| **Cloud** |  | [slurp](https://github.com/0xbharath/slurp) | Finding public S3 buckets

More cool tools:
* https://github.com/zardus/ctf-tools

## Noteworthy challenges

| Category | Event | Challenge |
| :------- | :---- | :-------- |

