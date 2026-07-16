import os
import re

files = [
    ("README.md", """## 📚 Recursos Recomendados

### Cursos Online
1. "[Nuclear and Particle Physics](https://ocw.mit.edu/courses/physics/8-701-introduction-to-nuclear-and-particle-physics-fall-2020/)" (MIT OpenCourseWare) - Un curso exhaustivo sobre las bases fenomenológicas y teóricas de la física nuclear y subatómica.
2. "[Particle Physics: an Introduction](https://www.coursera.org/learn/particle-physics)" (Coursera - University of Geneva) - Excelente introducción a la física de altas energías y al Modelo Estándar, sin requerir matemáticas avanzadas.
3. "[Understanding Nuclear Energy](https://www.edx.org/course/understanding-nuclear-energy)" (edX - Delft University) - Aborda los aspectos de la fisión, reactores nucleares, seguridad y ciclo del combustible.
4. "[The Standard Model of Particle Physics](https://online.stanford.edu/courses/sohs-yphys0001-standard-model-particle-physics)" (Stanford Online) - Un análisis en profundidad sobre los quarks, leptones y las fuerzas fundamentales.
5. "[Exploring Quantum Physics](https://www.coursera.org/learn/quantum-physics)" (Coursera - University of Maryland) - Explora la mecánica cuántica que es la base necesaria para comprender la física subatómica.
6. "[Introduction to Nuclear Engineering and Ionizing Radiation](https://ocw.mit.edu/courses/nuclear-engineering/22-01-introduction-to-nuclear-engineering-and-ionizing-radiation-fall-2016/)" (MIT OpenCourseWare) - Cubre las interacciones de radiación ionizante y aplicaciones en medicina y reactores.
7. "[Particle Physics](https://www.edx.org/course/particle-physics)" (edX) - Curso avanzado centrado en los descubrimientos modernos y aceleradores de partículas.
8. "[Astrophysics and Nuclear Physics](https://www.coursera.org/learn/astro-nuclear-physics)" (Coursera) - Relaciona los procesos nucleares con los fenómenos astrofísicos como las supernovas.
9. "[Quantum Field Theory](https://online.stanford.edu/courses/physics330-quantum-field-theory)" (Stanford University) - Curso fundamental para entender cómo las partículas surgen como excitaciones de campos.

### Artículos y Textos de Referencia
1. Griffiths, D. J. (2008). *[Introduction to Elementary Particles](https://www.wiley.com/en-us/Introduction+to+Elementary+Particles%2C+2nd%2C+Revised+Edition-p-9783527406012)*. Wiley-VCH. (Texto estándar para introducción a nivel de grado).
2. Krane, K. S. (1987). *[Introductory Nuclear Physics](https://www.wiley.com/en-us/Introductory+Nuclear+Physics%2C+3rd+Edition-p-9780471805533)*. John Wiley & Sons. (Referencia clásica en física nuclear).
3. Halzen, F., & Martin, A. D. (1984). *[Quarks and Leptons: An Introductory Course in Modern Particle Physics](https://www.wiley.com/en-us/Quarks+and+Leptons%3A+An+Introductory+Course+in+Modern+Particle+Physics-p-9780471887416)*. John Wiley & Sons.
4. Perkins, D. H. (2000). *[Introduction to High Energy Physics](https://doi.org/10.1017/CBO9780511809040)*. Cambridge University Press.
5. Thomson, M. (2013). *[Modern Particle Physics](https://doi.org/10.1017/CBO9781139525367)*. Cambridge University Press.
6. Martin, B. R., & Shaw, G. (2017). *[Particle Physics](https://www.wiley.com/en-us/Particle+Physics%2C+4th+Edition-p-9781118912164)*. John Wiley & Sons.
7. Weinberg, S. (1967). "[A Model of Leptons](https://doi.org/10.1103/PhysRevLett.19.1264)". *Physical Review Letters*. (Trabajo seminal en la teoría electrodébil).
8. Gell-Mann, M. (1964). "[A Schematic Model of Baryons and Mesons](https://doi.org/10.1016/S0031-9163(64)92001-3)". *Physics Letters*. (Propuesta original del modelo de quarks).
9. Higgs, P. W. (1964). "[Broken Symmetries and the Masses of Gauge Bosons](https://doi.org/10.1103/PhysRevLett.13.508)". *Physical Review Letters*. (Mecanismo de Higgs).
10. Wong, S. S. M. (1998). *[Introductory Nuclear Physics](https://www.wiley.com/en-us/Introductory+Nuclear+Physics%2C+2nd+Edition-p-9780471239734)*. Wiley.
11. Glashow, S. L. (1961). "[Partial-symmetries of weak interactions](https://doi.org/10.1016/0029-5582(61)90469-2)". *Nuclear Physics*. (Unificación de interacciones débiles y electromagnéticas).
12. Salam, A. (1968). "[Weak and Electromagnetic Interactions](https://www.nobelprize.org/prizes/physics/1979/salam/lecture/)". *Nobel Symposium*. (Completando el modelo electrodébil junto con Weinberg y Glashow).
13. Chadwick, J. (1932). "[The Existence of a Neutron](https://doi.org/10.1098/rspa.1932.0112)". *Proceedings of the Royal Society A*. (El descubrimiento del neutrón).
14. Meitner, L., & Frisch, O. R. (1939). "[Disintegration of Uranium by Neutrons: a New Type of Nuclear Reaction](https://doi.org/10.1038/143239a0)". *Nature*. (Explicación de la fisión nuclear).
15. Bethe, H. A. (1939). "[Energy Production in Stars](https://doi.org/10.1103/PhysRev.55.434)". *Physical Review*. (Explicación de la fusión en las estrellas)."""),
    ("Detectores_y_Aceleradores/README.md", """## 📚 Recursos

### Cursos Online
1. "[Particle Accelerators](https://learninghub.cern.ch/)" (CERN E-learning)
2. "[Detector Technologies for Particle Physics](https://ocw.mit.edu/courses/physics/8-811-particle-physics-ii-fall-2005/)" (MIT OCW)
3. "[Medical Applications of Particle Physics](https://www.coursera.org/learn/medical-applications-particle-physics)" (Coursera)
4. "[Data Analysis in High Energy Physics](https://www.edx.org/course/data-analysis-in-high-energy-physics)" (edX)
5. "[Instrumentation and Detection](https://online.stanford.edu/)" (Stanford Online)
6. "[Advanced Particle Accelerators](https://uspas.fnal.gov/)" (US Particle Accelerator School)

### Artículos y Simulaciones
1. "[The Large Hadron Collider: Harvest of Run 1](https://link.springer.com/book/10.1007/978-3-319-15001-7)" (Springer, 2015)
2. "[Particle Detectors](https://doi.org/10.1017/CBO9780511812606)" (Grupen & Shwartz, 2008)
3. "[Principles of Charged Particle Acceleration](https://onlinelibrary.wiley.com/)" (Stanley Humphries)
4. "[CERN Virtual Tour y Simulaciones](https://home.cern/resources/video/cern/cern-virtual-tour)"
5. "[The ATLAS Experiment at the CERN Large Hadron Collider](https://doi.org/10.1088/1748-0221/3/08/S08003)" (2008, JINST)
6. "[The CMS experiment at the CERN LHC](https://doi.org/10.1088/1748-0221/3/08/S08004)" (2008, JINST)
7. "[Simulador de Colisiones](https://phet.colorado.edu/en/simulations/category/physics)" (PhET)
8. "[Development of Silicon Strip Detectors](https://arxiv.org/)" (Review Article)

### 📖 Referencias Útiles y Bibliografía
- Leo, W. R. (1994). *[Techniques for Nuclear and Particle Physics Experiments](https://link.springer.com/book/10.1007/978-3-642-57920-2)*. Springer.
- Knoll, G. F. (2010). *[Radiation Detection and Measurement](https://www.wiley.com/en-us/Radiation+Detection+and+Measurement%2C+4th+Edition-p-9780470131480)*. John Wiley & Sons.
- Wiedemann, H. (2015). *[Particle Accelerator Physics](https://link.springer.com/book/10.1007/978-3-319-18317-6)*. Springer.
- Halzen, F., & Martin, A. D. (1984). *[Quarks and Leptons](https://www.wiley.com/en-us/Quarks+and+Leptons%3A+An+Introductory+Course+in+Modern+Particle+Physics-p-9780471887416)*. John Wiley & Sons."""),
    ("El_Modelo_Estandar_de_Particulas/README.md", """## 📚 Recursos Específicos

### Cursos Online
1. "[Particle Physics](https://ocw.mit.edu/courses/physics/8-701-introduction-to-nuclear-and-particle-physics-fall-2020/)" (MIT OCW)
2. "[The Discovery of the Higgs Boson](https://www.coursera.org/learn/higgs-boson)" (Coursera - University of Edinburgh)
3. "[Quantum Field Theory](https://online.stanford.edu/courses/physics330-quantum-field-theory)" (Stanford University / edX)
4. "[The Standard Model of Particle Physics](https://online.stanford.edu/)" (Stanford Online)
5. "[Symmetries, Particles and Fields](https://www.maths.cam.ac.uk/undergrad/course/symmetries-particles-and-fields)" (University of Cambridge)
6. "[Introduction to String Theory](https://ocw.mit.edu/courses/physics/8-821-string-theory-fall-2008/)" (MIT OCW)

### Artículos y Simulaciones
1. "[CERN Document Server y Open Data Portal](https://opendata.cern.ch/)"
2. "[PDG (Particle Data Group): The Review of Particle Physics](https://pdg.lbl.gov/)"
3. "[A Model of Leptons](https://doi.org/10.1103/PhysRevLett.19.1264)" (S. Weinberg, 1967)
4. "[Broken Symmetries and the Masses of Gauge Bosons](https://doi.org/10.1103/PhysRevLett.13.508)" (P. W. Higgs, 1964)
5. "[A Schematic Model of Baryons and Mesons](https://doi.org/10.1016/S0031-9163(64)92001-3)" (M. Gell-Mann, 1964)
6. "[Observation of a new particle in the search for the Standard Model Higgs boson](https://doi.org/10.1016/j.physletb.2012.08.020)" (ATLAS Collaboration, 2012)
7. "[Observation of a new boson at a mass of 125 GeV](https://doi.org/10.1016/j.physletb.2012.08.021)" (CMS Collaboration, 2012)
8. "[Partial-symmetries of weak interactions](https://doi.org/10.1016/0029-5582(61)90469-2)" (S. L. Glashow, 1961)
9. "[Quarks and Leptons Simulation](https://phet.colorado.edu/)" (PhET)

### 📖 Referencias Útiles y Bibliografía
- Halzen, F., & Martin, A. D. (1984). *[Quarks and Leptons: An Introductory Course in Modern Particle Physics](https://www.wiley.com/en-us/Quarks+and+Leptons%3A+An+Introductory+Course+in+Modern+Particle+Physics-p-9780471887416)*. John Wiley & Sons.
- Griffiths, D. J. (2008). *[Introduction to Elementary Particles](https://www.wiley.com/en-us/Introduction+to+Elementary+Particles%2C+2nd%2C+Revised+Edition-p-9783527406012)*. Wiley-VCH.
- Thomson, M. (2013). *[Modern Particle Physics](https://doi.org/10.1017/CBO9781139525367)*. Cambridge University Press.
- Perkins, D. H. (2000). *[Introduction to High Energy Physics](https://doi.org/10.1017/CBO9780511809040)*. Cambridge University Press."""),
    ("Estructura_Nuclear/README.md", """## 📚 Recursos

### Cursos Online
1. "[Nuclear Structure and Reactions](https://ocw.mit.edu/courses/physics/8-701-introduction-to-nuclear-and-particle-physics-fall-2020/)" (MIT OCW)
2. "[Introduction to Nuclear Physics](https://www.coursera.org/learn/nuclear-physics)" (Coursera)
3. "[Advanced Nuclear Physics](https://www.edx.org/)" (edX)
4. "[Nuclear Models and Decay](https://online.stanford.edu/)" (Stanford Online)
5. "[Many-Body Physics in Nuclear Systems](https://phys.washington.edu/)" (University of Washington)

### Artículos y Simulaciones
1. "[The Shell Model of the Nucleus](https://www.nobelprize.org/prizes/physics/1963/mayer/lecture/)" (Maria Goeppert Mayer, Nobel Lecture)
2. "[On the Structure of Atomic Nuclei](https://www.nobelprize.org/prizes/physics/1975/bohr/lecture/)" (A. Bohr and B. Mottelson)
3. "[Nuclear Structure Database](https://www.nndc.bnl.gov/)" (NNDC)
4. "[Collective Model of the Nucleus](https://doi.org/10.1103/RevModPhys.28.432)" (Review Article)
5. "[Build a Nucleus](https://phet.colorado.edu/en/simulations/build-a-nucleus)" (PhET Interactive Simulations)
6. "[Magic Numbers in Nuclear Structure](https://physicstoday.scitation.org/)" (Physics Today)
7. "[Isospin in Nuclear Physics](https://www.annualreviews.org/)" (Annual Review of Nuclear Science)
8. "[The Liquid Drop Model and Nuclear Fission](https://doi.org/10.1103/PhysRev.56.426)" (N. Bohr, J.A. Wheeler)

### 📖 Referencias Útiles y Bibliografía
- Krane, K. S. (1987). *[Introductory Nuclear Physics](https://www.wiley.com/en-us/Introductory+Nuclear+Physics%2C+3rd+Edition-p-9780471805533)*. John Wiley & Sons.
- Wong, S. S. M. (1998). *[Introductory Nuclear Physics](https://www.wiley.com/en-us/Introductory+Nuclear+Physics%2C+2nd+Edition-p-9780471239734)*. Wiley.
- Bohr, A., & Mottelson, B. R. (1998). *[Nuclear Structure](https://www.worldscientific.com/worldscibooks/10.1142/3530)*. World Scientific.
- Heyde, K. (1994). *[Basic Ideas and Concepts in Nuclear Physics](https://www.routledge.com/Basic-Ideas-and-Concepts-in-Nuclear-Physics-An-Introductory-Approach/Heyde/p/book/9780750305341)*. CRC Press."""),
    ("Estructura_Nuclear_y_Radiactividad/README.md", """## 📚 Recursos Específicos

### Cursos Online
1. "[Nuclear Physics Fundamentals](https://www.coursera.org/learn/nuclear-physics)" (Coursera)
2. "[Radiation and Radioactivity](https://www.edx.org/course/radiation-and-radioactivity)" (edX)
3. "[Applied Nuclear Physics](https://ocw.mit.edu/courses/nuclear-engineering/22-02-introduction-to-applied-nuclear-physics-spring-2012/)" (MIT OCW)
4. "[Introduction to Nuclear Science](https://online.stanford.edu/)" (Stanford Online)
5. "[Nuclear Reactions and Isotope Production](https://www.coursera.org/)" (Coursera)
6. "[Health Physics and Radiation Protection](https://www.edx.org/)" (edX)

### Artículos y Simulaciones
1. "[Radioactive Dating Game](https://phet.colorado.edu/en/simulations/radioactive-dating-game)" (PhET Interactive Simulations)
2. "[Nuclear Fission](https://phet.colorado.edu/en/simulations/nuclear-fission)" (PhET Interactive Simulations)
3. "[Radioactivity and transmutation of elements](https://www.jstor.org/stable/90831)" (Rutherford & Soddy, 1903)
4. "[Chart of Nuclides](https://www.nndc.bnl.gov/nudat3/)" (NNDC)
5. "[The Mass of the Neutron](https://doi.org/10.1038/129312a0)" (J. Chadwick, 1932)
6. "[On the Constitution of Atoms and Molecules](https://doi.org/10.1080/14786441308634955)" (N. Bohr, 1913)
7. "[Nuclear Data Sheets for A=1 to 294](https://www.nndc.bnl.gov/nds/)" (NNDC)
8. "[Beta Decay and the Neutrino Hypothesis](https://arxiv.org/abs/physics/0609139)" (W. Pauli, 1930)

### 📖 Referencias Útiles y Bibliografía
- Krane, K. S. (1987). *[Introductory Nuclear Physics](https://www.wiley.com/en-us/Introductory+Nuclear+Physics%2C+3rd+Edition-p-9780471805533)*. John Wiley & Sons.
- Turner, J. E. (2007). *[Atoms, Radiation, and Radiation Protection](https://www.wiley.com/en-us/Atoms%2C+Radiation%2C+and+Radiation+Protection%2C+3rd+Edition-p-9783527406067)*. Wiley-VCH.
- Lilley, J. (2001). *[Nuclear Physics: Principles and Applications](https://www.wiley.com/en-us/Nuclear+Physics%3A+Principles+and+Applications-p-9780471979364)*. Wiley.
- Knoll, G. F. (2010). *[Radiation Detection and Measurement](https://www.wiley.com/en-us/Radiation+Detection+and+Measurement%2C+4th+Edition-p-9780470131480)*. Wiley."""),
    ("Fision_y_Fusion/README.md", """## 📚 Recursos Específicos

### Cursos Online
1. "[Plasma Physics and Applications](https://www.edx.org/course/plasma-physics-and-applications)" (edX - EPFL)
2. "[Nuclear Reactor Physics Basics](https://www.coursera.org/learn/nuclear-reactor-physics)" (Coursera)
3. "[Energy Processing in Stars](https://ocw.mit.edu/courses/physics/8-284-modern-astrophysics-spring-2006/)" (University of Arizona OCW / MIT)
4. "[Introduction to Plasma Physics](https://ocw.mit.edu/courses/nuclear-engineering/22-611j-introduction-to-plasma-physics-i-fall-2003/)" (MIT OCW)
5. "[Fusion Energy: Principles and Technology](https://online.stanford.edu/)" (Stanford Online)
6. "[Advanced Nuclear Reactor Engineering](https://www.edx.org/)" (edX)

### Artículos y Simulaciones
1. "[ITER Educational Resources (Simulador Tokamak)](https://www.iter.org/education/)"
2. "[Energy production in stars](https://doi.org/10.1103/PhysRev.55.434)" (H. Bethe, 1939)
3. "[The Discovery of Nuclear Fission](https://doi.org/10.1038/143239a0)" (L. Meitner, O. R. Frisch, 1939)
4. "[IAEA Nuclear Data Section](https://www-nds.iaea.org/)"
5. "[The Mechanism of Nuclear Fission](https://doi.org/10.1103/PhysRev.56.426)" (N. Bohr and J. A. Wheeler, 1939)
6. "[Nuclear Fission](https://phet.colorado.edu/en/simulations/nuclear-fission)" (PhET Interactive Simulations)
7. "[Plasma confinement in Tokamaks](https://www.iter.org/mach/Tokamak)" (Review Article)
8. "[Inertial Confinement Fusion](https://lasers.llnl.gov/science/icf)" (NIF Publications)
9. "[Design and Operation of Pressurized Water Reactors](https://www.iaea.org/publications)" (IAEA Bulletin)

### 📖 Referencias Útiles y Bibliografía
- Lamarsh, J. R., & Baratta, A. J. (2001). *[Introduction to Nuclear Engineering](https://www.pearson.com/en-us/subject-catalog/p/introduction-to-nuclear-engineering/P200000006763)*. Prentice Hall.
- Chen, F. F. (1984). *[Introduction to Plasma Physics and Controlled Fusion](https://link.springer.com/book/10.1007/978-1-4757-5595-4)*. Springer.
- Krane, K. S. (1987). *[Introductory Nuclear Physics](https://www.wiley.com/en-us/Introductory+Nuclear+Physics%2C+3rd+Edition-p-9780471805533)*. John Wiley & Sons.
- Stacey, W. M. (2010). *[Fusion Plasma Physics](https://www.wiley.com/en-us/Fusion+Plasma+Physics%2C+2nd+Edition-p-9783527411344)*. Wiley-VCH."""),
    ("Modelo_Estandar/README.md", """## 📚 Recursos

### Cursos Online
1. "[The Standard Model](https://ocw.mit.edu/courses/physics/8-701-introduction-to-nuclear-and-particle-physics-fall-2020/)" (MIT OCW)
2. "[Particle Physics: An Introduction](https://www.coursera.org/learn/particle-physics)" (Coursera)
3. "[Beyond the Standard Model](https://www.edx.org/)" (edX)
4. "[Quantum Electrodynamics and Chromodynamics](https://online.stanford.edu/)" (Stanford Online)
5. "[Symmetry and the Standard Model](https://www.maths.cam.ac.uk/)" (University of Cambridge)

### Artículos y Simulaciones
1. "[A Model of Leptons](https://doi.org/10.1103/PhysRevLett.19.1264)" (S. Weinberg, 1967)
2. "[Broken Symmetries and the Masses of Gauge Bosons](https://doi.org/10.1103/PhysRevLett.13.508)" (P. W. Higgs, 1964)
3. "[The Discovery of the Top Quark](https://www.fnal.gov/pub/science/top-quark.html)" (Fermilab)
4. "[CERN Open Data Portal - Standard Model Analyses](https://opendata.cern.ch/)"
5. "[Neutrino Oscillations](https://doi.org/10.1103/PhysRevLett.81.1562)" (Super-Kamiokande, 1998)
6. "[Elementary Particles](https://phet.colorado.edu/)" (PhET Interactive Simulations)
7. "[CP Violation in the Kaon System](https://doi.org/10.1103/PhysRevLett.13.138)" (Cronin & Fitch, 1964)
8. "[Quantum Chromodynamics at high energies](https://doi.org/10.1103/RevModPhys.67.157)" (Review Article)

### 📖 Referencias Útiles y Bibliografía
- Halzen, F., & Martin, A. D. (1984). *[Quarks and Leptons](https://www.wiley.com/en-us/Quarks+and+Leptons%3A+An+Introductory+Course+in+Modern+Particle+Physics-p-9780471887416)*. John Wiley & Sons.
- Griffiths, D. J. (2008). *[Introduction to Elementary Particles](https://www.wiley.com/en-us/Introduction+to+Elementary+Particles%2C+2nd%2C+Revised+Edition-p-9783527406012)*. Wiley-VCH.
- Thomson, M. (2013). *[Modern Particle Physics](https://doi.org/10.1017/CBO9781139525367)*. Cambridge University Press.
- Schwartz, M. D. (2014). *[Quantum Field Theory and the Standard Model](https://doi.org/10.1017/CBO9781139048040)*. Cambridge."""),
    ("Radioactividad_y_Decaimientos/README.md", """## 📚 Recursos

### Cursos Online
1. "[Radioactivity and Health Physics](https://ocw.mit.edu/courses/nuclear-engineering/22-01-introduction-to-nuclear-engineering-and-ionizing-radiation-fall-2016/)" (MIT OCW)
2. "[Introduction to Radiation Shielding](https://www.coursera.org/)" (Coursera)
3. "[Nuclear Decay and Dosimetry](https://www.edx.org/)" (edX)
4. "[Medical Applications of Radiation](https://online.stanford.edu/)" (Stanford Online)
5. "[Environmental Radioactivity](https://www.u-tokyo.ac.jp/en/)" (University of Tokyo)

### Artículos y Simulaciones
1. "[The Radioactivity of Uranium](https://gallica.bnf.fr/ark:/12148/bpt6k30784/f420.item)" (H. Becquerel, 1896)
2. "[Polonium and Radium Discovery](https://gallica.bnf.fr/ark:/12148/bpt6k3083t/f1215.item)" (M. Curie & P. Curie, 1898)
3. "[Alpha Decay](https://phet.colorado.edu/en/simulations/alpha-decay)" (PhET Interactive Simulations)
4. "[Beta Decay](https://phet.colorado.edu/en/simulations/beta-decay)" (PhET Interactive Simulations)
5. "[Chart of Nuclides](https://www.nndc.bnl.gov/nudat3/)" (NNDC)
6. "[Biological Effects of Ionizing Radiation](https://nap.nationalacademies.org/catalog/11340/health-risks-from-exposure-to-low-levels-of-ionizing-radiation)" (BEIR Reports)
7. "[Geiger-Nuttall Law for Alpha Decay](https://doi.org/10.1080/14786441008637156)" (Review)
8. "[Neutrino Detection from Beta Decay](https://doi.org/10.1126/science.124.3212.103)" (Reines & Cowan, 1956)

### 📖 Referencias Útiles y Bibliografía
- Krane, K. S. (1987). *[Introductory Nuclear Physics](https://www.wiley.com/en-us/Introductory+Nuclear+Physics%2C+3rd+Edition-p-9780471805533)*. John Wiley & Sons.
- Turner, J. E. (2007). *[Atoms, Radiation, and Radiation Protection](https://www.wiley.com/en-us/Atoms%2C+Radiation%2C+and+Radiation+Protection%2C+3rd+Edition-p-9783527406067)*. Wiley-VCH.
- Knoll, G. F. (2010). *[Radiation Detection and Measurement](https://www.wiley.com/en-us/Radiation+Detection+and+Measurement%2C+4th+Edition-p-9780470131480)*. Wiley.
- Evans, R. D. (1955). *[The Atomic Nucleus](https://archive.org/details/atomicnucleus0000evan)*. McGraw-Hill.""")
]

for file_path, new_content in files:
    full_path = file_path
    if not os.path.exists(full_path):
        print(f"Error: {full_path} not found")
        continue
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'## 📚 Recursos.*', content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_content + '\n'
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {full_path}")
    else:
        print(f"Could not find '## 📚 Recursos' in {full_path}")
