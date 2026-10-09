# COA — Computer Organization & Architecture

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-2f6fde?logo=githubpages&logoColor=white)](https://mohit-verma1411.github.io/coa-notes/)
[![Mermaid](https://img.shields.io/badge/flowcharts-32-45a1ff)](https://mohit-verma1411.github.io/coa-notes/COA%20Notes%20-%20Unit%201%20%26%20Unit%202.html)
[![License](https://img.shields.io/badge/source-Mano%203rd%20ed.-lightgrey)](https://github.com/Mohit-Verma1411/coa-notes)

**Complete study notes for Unit 1 & Unit 2, with 32 flowcharts.**

> **🌐 Read it live:** <https://mohit-verma1411.github.io/coa-notes/>

> Source: M. Morris Mano, *Computer System Architecture*, 3rd Edition.
> Companion topics (Von Neumann architecture, computer generations, MIPS/MFLOPS,
> Amdahl's law, "make the common case fast") are not in Mano and are marked in the
> notes as coming from standard architecture references.

---

## 📖 How to read the notes

| | File | Notes |
|---|---|---|
| **HTML (recommended)** | [**Open the notes**](./COA%20Notes%20-%20Unit%201%20%26%20Unit%202.html) | All 32 flowcharts render automatically. Works **fully offline** (`mermaid.min.js` is bundled). Use **Ctrl+P** for a PDF-ready printout. |
| **Markdown** | [`COA Notes - Unit 1 & Unit 2.md`](./COA%20Notes%20-%20Unit%201%20%26%20Unit%202.md) | Source of truth — editable in Obsidian, VS Code, Typora or GitHub. Flowcharts are Mermaid code blocks. |

After cloning, just double-click the `.html` file — no server or internet needed.

---

## 🗺️ Syllabus covered

### Unit 1 — Data Representation and Computer Arithmetic
- Introduction to Computer Systems, **Organization vs Architecture vs Design**
- **Von Neumann architecture**, stored-program concept, evolution & computer generations
- Data representation: number systems, complements, **fixed point**, **floating point**,
  **decimal (BCD)** arithmetic, Gray/ASCII/parity codes
- Digital arithmetic algorithms: **addition, subtraction** (signed-magnitude and 2's
  complement), **multiplication**, **Booth's algorithm** (with worked example), division,
  floating-point and BCD operations
- **Multiprocessors and Multicomputer**, interconnection structures
- **MIPS, MFLOPS**, CPI, CPU execution time
- **Memory Organization**: memory hierarchy, types of memory, cache memory,
  virtual memory, **TLB**

### Unit 2 — Basic Computer Organization and Design
- General register organization, **stack organization**, **common bus system**
- Computer instructions (25 instructions), **timing and control**
- Input, output and **interrupt — interrupt cycle**, priority interrupt, daisy chain
- **Design drivers**: make the common case fast, **Amdahl's law**
- **Microprogrammed control organization**: control memory, address sequencing,
  microinstruction format, **horizontal vs vertical micro-programming**,
  design of the control unit, **micro program sequencer**
- **Hardwired vs micro-programmed** control
- **CISC vs RISC**: features and comparison, overlapped register windows

---

## 📊 The 32 flowcharts

1. Master syllabus map
2. Five functional units of a computer
3. Von Neumann machine block diagram
4. Fetch – Decode – Execute cycle
5. Computer generations
6. Decimal → binary conversion (radix conversion)
7. Floating-point operation (align → operate → normalize)
8. Signed-magnitude add / subtract (Fig. 10-2)
9. Signed 2's-complement add / subtract (Fig. 10-4)
10. Signed-magnitude multiplication (Fig. 10-6)
11. **Booth's algorithm (Fig. 10-8)**
12. BCD (+6 correction) adder
13. Multiprocessor interconnection networks
14. Memory hierarchy
15. Classification of memory
16. Cache hit / miss access
17. Virtual memory & page fault
18. **TLB — segmented-page address translation (Fig. 12-21)**
19. Common bus system
20. Instruction formats (memory / register / I/O)
21. Timing and control unit
22. **Basic-computer instruction cycle (Fig. 5-9 / 5-15)**
23. Memory-reference instruction execution (Fig. 5-11)
24. Programmed polling vs interrupt-driven I/O
25. **Interrupt cycle (Fig. 5-13)**
26. Daisy-chain priority interrupt
27. Amdahl's law decision flow
28. Microprogrammed control unit organization (Fig. 7-1)
29. Control-memory address sequencing (Fig. 7-2)
30. **Microprogram sequencer (Fig. 7-8)**
31. Hardwired vs microprogrammed control
32. CISC vs RISC design choice

---

## 🔁 Regenerating the HTML

The HTML is generated from the Markdown, so edit the `.md`, then rebuild:

```bash
pip install markdown          # one-time
python3 build_html.py
```

`build_html.py` converts the Markdown, pulls out the Mermaid blocks, and writes
`COA Notes - Unit 1 & Unit 2.html` (which loads the bundled `mermaid.min.js`).

---

## 📚 References

- M. Morris Mano, *Computer System Architecture*, 3rd Edition (Prentice Hall) — primary source, chapters 3, 5, 7, 8, 10, 11, 12, 13.
- Standard computer architecture references for Von Neumann, generations, performance metrics and Amdahl's law.
- Diagrams rendered with [Mermaid](https://mermaid.js.org/).
