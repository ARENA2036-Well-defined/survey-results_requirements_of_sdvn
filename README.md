# Industrial Requirements for Software-defined Value Networks: Survey Results

This repository contains the survey results regarding industrial requirements for Software-defined Value Networks (SDVN), which was conducted among industrial partners of [ARENA2036](https://arena2036.de/), a research campus for future mobility and automotive production in Stuttgart.
An evaluation of the results and the motivation of SDVN can be found in an according [papers](#references)

## About the Survey
SDVN aim to increase flexibility, value-chain resilience through redundancy, scalability through standardized linkages and data formats as well as data consistency for sustainability requirements such as the CO2 footprint, as opposed to current Global Value Chains. 
Industrial requirements and the potential success of implementing SDVN are assesed in the survey. 
The survey was conducted with two representatives from each
company, one from the management and one from the technical department, who are interviewed about SDVNs.
The survey covers the interviewee’s experience with automation systems, the use of emerging technologies throughout the company’s value chains, perceived risks, sustainability factors, the potential of existing value chains, and requirements for further automation in SDVNs.
The survey highlights the industrial requirements, benefits, and research gaps for the future use of SDVNs in companies related to the automotive industry.

## Installation

Install [Python](https://python.org) (at least V3.10)

Clone or download this repository and if wanted create and activate a virtual environment for python in its folder.
```bash
python -m venv venv
venv\Scripts\activate.bat
```

Install the required libraries with pip.
```bash
pip install -r requirements.txt
```

Run the python script containig the Web-UI
```bash
python main.py
```
After a short startup your browser should open on [http://localhost:8080](http://localhost:8080) with the interactive evaluation tool of the survey.

## Usage

The UI shows the results of the survey.
Single choice questions are illustrated with pie charts, multiple choice questions with bar charts.
The results are on top shown in tabular form and optional entered text input is displayed.

The header offers the possibility to filter for specific answers to questions.
To do so first a question has to be chosen and afterwards a single of the provided answer possibilities can be selected.
The filter can be reset using the delete button.

The raw files of the questions and the surveys are included in the repository.
These list all questions with their possible answers and surveys with their responses individually and can be used for further evaluations.

## Author

David Dietrich, Research Assistant „Mechatronic Systems and Processes“, Institute for Control Engineering of Machine Tools and Manufacturing Units (ISW), University of Stuttgart

## References

D. Dietrich et al., "Software-defined Value Networks: Industrial Requirements and Research Gap" (in press) 

D. Dietrich, M. Zürn, C. Reiff, M. Neubauer, A. Lechler, and A. Verl, “Software-Defined Value Networks: Motivation, Approaches, and Research Activities,” in Production at the Leading Edge of Technology (T. Bauernhansl, A. Verl, M. Liewald, and H.-C. Möhring, eds.), Lecture Notes in Production Engineering, pp. 514–524, Cham: Springer Nature Switzerland, 2024

## License
Shield: [![CC BY-ND 4.0][cc-by-nd-shield]][cc-by-nd]

This work is licensed under a
[Creative Commons Attribution-NoDerivs 4.0 International License][cc-by-nd].

[![CC BY-ND 4.0][cc-by-nd-image]][cc-by-nd]

[cc-by-nd]: https://creativecommons.org/licenses/by-nd/4.0/
[cc-by-nd-image]: https://licensebuttons.net/l/by-nd/4.0/88x31.png
[cc-by-nd-shield]: https://img.shields.io/badge/License-CC%20BY--ND%204.0-lightgrey.svg

