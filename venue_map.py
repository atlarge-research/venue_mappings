import re
from enum import Enum


class MatchType(Enum):
    EXACT = 1
    STARTS_WITH = 2
    ENDS_WITH = 3
    CONTAINS = 4
    REGEX = 5


class VenueMapper(object):
    venues = {
        "AISTATS": {
            (r"AISTATS", MatchType.EXACT),
            (r"{AISTATS}", MatchType.CONTAINS),
            (r"Learning from Data", MatchType.EXACT),
            (r"International Conference on Artificial Intelligence and Statistics", MatchType.EXACT),
            (r"International Workshop on Artificial Intelligence and Statistics,", MatchType.CONTAINS),
        },
        "SIGCSE": {
            (r"SIGSCSE", MatchType.EXACT),  # DBLP
            (r"{SIGCSE}", MatchType.CONTAINS),
            (r"ACM Technical Symposium on Computer Science Education", MatchType.CONTAINS),
        },
        "CloudComp": {
            (r"CloudComp", MatchType.EXACT),  # DBLP
            (r"International Conference, CloudComp", MatchType.CONTAINS),
            (r"International Conference on Cloud Computing", MatchType.EXACT),
        },
        "FedCSIS": {
            (r"FedCSIS", MatchType.EXACT),
            (r"Federated Conference on Computer Science and Information Systems", MatchType.CONTAINS),
        },
        "PSI": {
            (r"{PSI}", MatchType.CONTAINS),
            (r"Perspectives of System Informatics", MatchType.STARTS_WITH),
            (r"International Sympoisum on Theoretical Programming", MatchType.STARTS_WITH),
            (r"International Symposium on Theoretical Programming", MatchType.STARTS_WITH),
            (r"Ershov Memorial Conference", MatchType.CONTAINS),
        },
        "ISPA": {
            (r"ISPA", MatchType.EXACT),
            (r"{ISPA}", MatchType.CONTAINS),
            (
                r"^(?=.*International Symposium on Parallel and Distributed Processing with Applications)(?!.*\bWorkshops\b).*$",
                MatchType.REGEX),
        },
        "IBMRD": {
            (r"IBMRD", MatchType.EXACT),
            (r"{IBM} Journal of Research and Development", MatchType.CONTAINS),
            (r"IBM Journal of Research and Development", MatchType.CONTAINS),
        },
        "ICDCS": {
            (r"ICDCS", MatchType.EXACT),  # used by DBLP
            (r"International Conference on Distributed Computing Systems,", MatchType.CONTAINS),
            (r"International Conference on Distributed Computing Systems {(ICDCS}", MatchType.CONTAINS),
            (r"International Conference on Distributed Computing Systems (ICDCS)", MatchType.CONTAINS),
            (r"Distributed Computing Systems,", MatchType.STARTS_WITH),
        },
        "OSDI": {
            (r"OSDI", MatchType.EXACT),  # used by DBLP
            (r"Symposium on Operating Systems Design and Implementation", MatchType.CONTAINS),
        },
        "ICFEC": {
            (r"ICFEC", MatchType.EXACT),
            (r"{ICFEC}", MatchType.CONTAINS),
            (r"(ICFEC)", MatchType.CONTAINS),
        },
        "CVPR": {
            (r"^CVPR( \(\d\))?$", MatchType.REGEX),
            (r"(CVPR)", MatchType.CONTAINS),
            (r"\{CVPR\} (?!Workshops)", MatchType.REGEX),
        },
        "JPDC": {
            (r"J. Parallel Distrib. Comput.", MatchType.EXACT),  # Used by DBLP
            (r"Journal of Parallel and Distributed Computing", MatchType.EXACT),
        },
        # "IFIP": {
        #     "IFIP"
        # },
        "POPL": {
            (r"POPL", MatchType.EXACT),  # DBLP
            (r"(S|s)ymposium on Principles of (P|p)rogramming (L|l)anguages", MatchType.REGEX),
        },
        "SOSP": {
            (r"SOSP", MatchType.EXACT),  # DBLP
            (r"{SOSP}", MatchType.CONTAINS),
            (r"Symposium on Operating Systems Principles", MatchType.CONTAINS),
            (r"symposium on Operating systems principles", MatchType.CONTAINS),  # Google Scholar, lower case
        },
        "P2P": {
            (r"P2P", MatchType.EXACT),
            (r"{(P2P}", MatchType.CONTAINS),
            (r"{P2P}", MatchType.CONTAINS),
            (r"(P2P)", MatchType.CONTAINS),
            (r"Peer-to-Peer Computing", MatchType.EXACT),
        },
        "ICCSE": {
            (r"ICCSE", MatchType.EXACT),
            (r"{ICCSE}", MatchType.CONTAINS),
            (r"International Conference on Crowd Science and Engineering", MatchType.ENDS_WITH),
        },
        "TPDS": {
            (r"Trans. Parallel Distrib. Syst.", MatchType.ENDS_WITH),
            (r"Transactions on Parallel and Distributed Systems", MatchType.CONTAINS),
            (r"Transactions on parallel and distributed systems", MatchType.CONTAINS),
        },
        "SERVICES": {
            (r"^SERVICES( (I|II))?$", MatchType.REGEX),
            (r"{SERVICES}", MatchType.CONTAINS),
            (r"(SERVICES)", MatchType.CONTAINS),
            (r"IEEE SCW", MatchType.EXACT),
            (r"^(?=.*\bServices(-Part)?\b)(?=.*\bCongress on\b).*$", MatchType.REGEX),
        },
        "TOPLAS": {
            (r"TOPLAS", MatchType.EXACT),
            (r"Trans. Program. Lang. Syst.", MatchType.ENDS_WITH),
            (r"(TOPLAS)", MatchType.CONTAINS),
        },
        "WORKS": {
            (r"SC-WORKS", MatchType.EXACT),
            (r"{WORKS}", MatchType.CONTAINS),
            (r"(w|W)orkshop on Workflows in (s|S)upport of (l|L)arge-(s|S)cale (s|S)cience", MatchType.REGEX),
            (r"Workflows in support of large-scale science", MatchType.EXACT),
        },
        "NDSS": {
            (r"NDSS", MatchType.EXACT),
            (r"(NDSS)", MatchType.CONTAINS),
            (r"\{(\(S\))?NDSS\}", MatchType.REGEX),
            (r"^(?=.*\bNetwork and Distributed System Security\b)(?=.*\bSymposium\b).*$", MatchType.REGEX),
        },
        "MOBILESoft": {
            (r"MOBILESoft", MatchType.EXACT),
            (r"International Conference on Mobile Software Engineering and Systems(,|$)", MatchType.REGEX),
        },
        "CCGrid": {
            (r"CCGrid", MatchType.EXACT),  # used by DBLP
            (r"CCGRID", MatchType.EXACT),  # also used by DBLP
            (r"International Symposium on Cluster, Cloud and Grid Computing,", MatchType.CONTAINS),
            (r"International Symposium on Cluster Computing and the Grid", MatchType.CONTAINS),
            (r"International Symposium on Cluster, Cloud and Grid Computing", MatchType.CONTAINS),
        },
        "NOSSDAV": {
            (r"NOSSDAV", MatchType.EXACT),
            (r"Network and Operating System Support for Digital Audio and Video,", MatchType.CONTAINS),
            (r"Network and Operating System Support for Digital Audio and Video", MatchType.ENDS_WITH),
        },
        "ISWC": {
            (r"ISWC", MatchType.EXACT),
            (r"{ISWC}", MatchType.CONTAINS),
            (r"{(ISWC}", MatchType.CONTAINS),
            (r"^(?=.*\bWearable Computers\b)(?=.*\bInternational Symposium\b).*$", MatchType.REGEX),
        },
        "IPDPS": {
            (r"IPDPS", MatchType.EXACT),  # used by DBLP
            (r"{IPDPS}", MatchType.CONTAINS),
            (r"Parallel and Distributed Processing Symposium,", MatchType.CONTAINS),
            (r"International Parallel and Distributed Processing Symposium {(IPDPS}", MatchType.CONTAINS),
            # Tricky one, as workshops use the same booktitle.
        },
        "WOWMOM": {
            (r"WoWMoM", MatchType.EXACT),  # DBLP
            (r"WOWMOM", MatchType.EXACT),
            (r"(i|I)nternational workshop on Wireless mobile multimedia(,|$)", MatchType.REGEX),
            (r"{WOWMOM}", MatchType.CONTAINS),
            (r"{(WOWMOM}", MatchType.CONTAINS),
            (r"^(?=.*\bWorld of Wireless,? Mobile and Multimedia Networks\b)(?=.*\bSymposium\b).*$", MatchType.REGEX),
        },
        "SPW": {
            (r"SPW", MatchType.EXACT),
            (r"Security Protocols Workshop", MatchType.EXACT),
            (r"^(?=.*\bInternational Workshop\b( on|,))(?=.*\bSecurity Protocols\b).*$", MatchType.REGEX),
        },
        "JSSPP": {
            (r"JSSPP", MatchType.EXACT),
            (r"{JSSPP}", MatchType.CONTAINS),
            (r"Job Scheduling Strategies for Parallel Processing(,|$)", MatchType.REGEX),
        },
        "UCC": {
            (r"UCC", MatchType.EXACT),
            (r"(UCC)", MatchType.CONTAINS),
            (r"^(?=.*\{UCC\})(?!.*\bCompanion\b).*$", MatchType.REGEX),
        },
        "ISCID": {
            (r"^ISCID( \(\d\))?$", MatchType.REGEX),
            (r"^(?=.*\bInternational Symposium on)(?=.*\bComputational Intelligence and Design\b).*$", MatchType.REGEX),
        },
        "SIGMETRICS": {
            (r"SIGMETRICS", MatchType.EXACT),
            (r"{SIGMETRICS}", MatchType.CONTAINS),
            (r"SIGMETRICS (Abstracts)", MatchType.CONTAINS),
            (r"SIGMETRICS conference on Computer performance modeling measurement and evaluation", MatchType.ENDS_WITH),

        },
        "EDBT": {
            (r"EDBT", MatchType.EXACT),
            (r"\(EDBT/ICDT \d{4}\)", MatchType.REGEX),
            (r"\{\(EDBT/ICDT\} \d{4}\)", MatchType.REGEX),
            (r"International Conference on Extending Database Technology,", MatchType.CONTAINS),
            (r"International Conference on Extending Database Technology", MatchType.ENDS_WITH),
        },
        "ICWS": {
            (r"ICWS", MatchType.EXACT),  # DBLP
            (r"ICWS-Europe", MatchType.EXACT),  # DBLP
            (r"ICWS Computer Society", MatchType.EXACT),
            (r"\(ICWS'\d{2}\)", MatchType.REGEX),
            (r"^(?=.*\bInternational Conference on)(?=.*\bWeb Services\b)(?!.*\bPractices\b).*$", MatchType.REGEX),
        },
        "CLOUD": {
            (r"^(IEEE )?CLOUD$", MatchType.REGEX),  # DBLP
            (r"{CLOUD}", MatchType.CONTAINS),
            (r"(CLOUD)", MatchType.CONTAINS),
            (r"International Conference on Cloud Computing", MatchType.ENDS_WITH),

        },
        "FiCloud": {
            (r"FiCloud", MatchType.EXACT),
            (r"(FiCloud)", MatchType.CONTAINS),
            (r"International Conference on Future Internet of Things and Cloud,", MatchType.CONTAINS),
        },
        "GCC": {
            (r"GCC", MatchType.EXACT),
            (r"^GCC \(\d\)$", MatchType.REGEX),
            (r"\{GCC\} (?!.*\bWorkshops\b)", MatchType.REGEX),
            (r"International Conference on Grid and Cooperative Computing(,|$)", MatchType.REGEX),
        },
        "SIGCOMM": {
            (r"SIGCOMM", MatchType.EXACT),
            (r"\{SIGCOMM\} (?!.*\bworkshop\b)", MatchType.REGEX),
            (r"ACM SIGCOMM Computer Communication Review", MatchType.EXACT),
            (r"ACM Special Interest Group on Data Communication", MatchType.ENDS_WITH),
        },
        "SIGMOD": {
            (r"SIGMOD Conference", MatchType.EXACT),
            (r"SIGMOD", MatchType.EXACT),
            (r"{SIGMOD}", MatchType.CONTAINS),
            (r"(i|I)nternational (c|C)onference on Management of (d|D)ata$", MatchType.REGEX),
            (r"SIGMOD'\d{2}", MatchType.REGEX),
            (r"Association for Computing Machinery Special Interest Group on Management of Data", MatchType.CONTAINS),
        },
        "SoCC": {
            (r"SoCC", MatchType.EXACT),
            (r"(s|S)ymposium on Cloud (c|C)omputing(, SoCC|$)", MatchType.REGEX),
        },
        "ICPE": {
            (r"ICPE", MatchType.EXACT),
            (r"{WOSP}", MatchType.CONTAINS),
            (r"^(?=.*\bICPE\b)(?!.*\bCompanion\b)(?!.*\bworkshop\b)(?!.*\bECCE\b).*$", MatchType.REGEX),
            (r"international workshop on Software and performance", MatchType.ENDS_WITH),
            (r"{WOSP/SIPEW}", MatchType.CONTAINS),
        },
        "SSDBM": {
            (r"SSDBM", MatchType.EXACT),  # DBLP
            (r"\{\(SSDBM\} \d{4}\)", MatchType.REGEX),
            (r"{LBL} Workshop on Statistical Database Management,", MatchType.CONTAINS),
            (r"International Workshop on Statistical and Scientific Database Management,", MatchType.CONTAINS),
            (r"International Workshop on Statistical Database Management,", MatchType.CONTAINS),
        },
        # "IDEAS": {
        #     "IDEAS",
        #     "International Database Engineering {&} Applications Symposium"
        # },
        "GRADES@SIGMOD-PODS": {
            (r"GRADES@SIGMOD/PODS", MatchType.CONTAINS),
            (r"International Workshop on Graph Data-management Experiences {\&} Systems", MatchType.CONTAINS),
            (r"International Workshop on Graph Data-management Experiences {&} Systems", MatchType.CONTAINS),
        },
        "HPDC": {
            (r"HPDC", MatchType.EXACT),
            (r"{HPDC}", MatchType.CONTAINS),
            (r"{(HPDC}", MatchType.CONTAINS),
            (r"International Symposium on High Performance Distributed Computing,", MatchType.CONTAINS),
            (r"High-Performance Distributed Computing,", MatchType.STARTS_WITH),  # Notice the carrot.
            (r"International Symposium on High Performance Parallel and Distributed Computing,", MatchType.CONTAINS),
            (r"International Symposium on High-Performance Parallel and Distributed Computing,", MatchType.CONTAINS),
        },
        "AI-Science": {  # HPDC workshop
            (r"AI-Science@HPDC", MatchType.CONTAINS),
            (r"International Workshop on Autonomous Infrastructure for Science,", MatchType.CONTAINS),
        },
        "ScienceCloud": {  # HPDC workshop
            (r"ScienceCloud@HPDC", MatchType.CONTAINS),
            (r"Workshop on Scientific Cloud Computing,", MatchType.CONTAINS),
        },
        "ROSS": {  # HPDC workshop
            (r"ROSS@HPDC", MatchType.CONTAINS),
            (r"International Workshop on Runtime and Operating Systems for Supercomputers,", MatchType.CONTAINS),
        },
        "GRID": {
            (r"GRID", MatchType.EXACT),
            (r"{GRID}", MatchType.CONTAINS),
            (r"(GRID)", MatchType.CONTAINS),
            (r"International Workshop on Grid Computing", MatchType.EXACT),
            (r"International Conference on Grid Computing,", MatchType.CONTAINS),
        },
        # "BroadNets": {
        #     "BroadNets",
        #     "International Conference on Broadnets Networks"
        # },
        # "WOOT": {
        #     "WOOT",
        #     "USENIX workshop on Offensive Technologies"
        # },
        # "CACM": {
        #     "CACM",
        #     "Communications of the ACM"
        # },
        "IC": {
            (r"IC", MatchType.EXACT),
            (r"IEEE Internet Computing", MatchType.EXACT),
            (r"{IEEE} Internet Computing", MatchType.EXACT),
        },
        "ICAC": {
            (r"ICAC", MatchType.EXACT),
            (r"International Conference on Autonomic Computing,", MatchType.CONTAINS),
            (r"{ICAC}", MatchType.CONTAINS),
            (r"\{\(ICAC} \d+\)", MatchType.REGEX),
        },
        "Euro-Par": {
            (r"^Euro-(p|P)ar( \(\d\))?$", MatchType.REGEX),
            (r"European Conference on Parallel Processing", MatchType.EXACT),
            (r"International Euro-Par Conference", MatchType.CONTAINS),
            (r"^(?=.*\bEuro-Par\b)(?=.*\bInternational Conference on Parallel and Distributed Computing\b).*$",
             MatchType.REGEX),
        },
        "NSDI": {
            (r"NSDI", MatchType.EXACT),  # used by DBLP
            (r"Symposium on Networked Systems Design and Implementation", MatchType.CONTAINS),
        },
        # "WWW": {
        #     "WWW",
        #     "International Conference on World Wide Web Companion"
        # },
        "FGCS": {
            (r"FGCS", MatchType.EXACT),
            (r"Future Generation Computer Systems", MatchType.EXACT),
            (r"Future Generation Comp. Syst.", MatchType.CONTAINS),
        },
        "EuroSys": {
            (r"EuroSys", MatchType.EXACT),  # DBLP
            (r"ACM SIGOPS Operating Systems Review", MatchType.EXACT),
            (r"European conference on Computer systems,", MatchType.CONTAINS),
            (r"EuroSys Conference,", MatchType.CONTAINS),
        },
        "ISPDC": {
            (r"ISPDC", MatchType.EXACT),
            (r"{ISPDC}", MatchType.CONTAINS),
            (r"{(ISPDC}", MatchType.CONTAINS),
            (r"(ISPDC)", MatchType.CONTAINS),
        },
        # "MobiCom": {
        #     "MobiCom",
        #     "International Conference on Mobile Computing and Networking"
        # },
        "IC2E": {
            (r"IC2E", MatchType.EXACT),
            (r"\{IC2E\} (?!.*\bWorkshops\b).*", MatchType.REGEX),
            (r"(IC2E)", MatchType.CONTAINS),
        },
        "CLUSTER": {
            (r"CLUSTER", MatchType.EXACT),  # used by DBLP
            (r"{CLUSTER}", MatchType.CONTAINS),
            (r"Cluster Computing, \d{4}\.", MatchType.REGEX),  # Google scholar
            (r"International Conference on Cluster Computing,", MatchType.CONTAINS),
            (r"International Conference on Cluster Computing {(CLUSTER}", MatchType.CONTAINS),
        },
        # "AINA": {
        #     "AINA",
        #     "Advanced Information Networking and Applications"
        # },
        "SC": {
            (r"SC", MatchType.EXACT),  # used by DBLP
            (r"{SC2005}", MatchType.CONTAINS),  # Funny mislabeling from the past.
            (r"Proceedings Supercomputing ", MatchType.STARTS_WITH),
            (r"SC State of the Practice Reports", MatchType.EXACT),  # DBLP
            (r"{ACM/IEEE} Conference on Supercomputing,", MatchType.CONTAINS),
            (r"^(?=.*International Conference for High Performance Computing,)(?!.*\bWorkshop\b).*$", MatchType.REGEX),
        },
        # "HPC": {
        #     r"High-Performance Computing in China:",
        # },
        # "MMVE": {
        #     "MMVE",
        #     "International Workshop on Massively Multiusers Virtual Environment"
        # },
        # "GLOBECOM": {
        #     "GLOBECOM"
        # },
        "ATC": {
            (r"{ATC}", MatchType.CONTAINS),
            (r"Proc. of ATC", MatchType.EXACT),
            (r"{USENIX} Summer Conference", MatchType.CONTAINS),
            (r"Usenix Winter \d{4} Technical Conference,", MatchType.REGEX),
            (r"Technical Conference on {UNIX} and Advanced Computing Systems,", MatchType.CONTAINS),
            (r"{FREENIX} Track:", MatchType.CONTAINS),
            (r"USENIX Annual Technical Conference", MatchType.EXACT),  # used by DBLP
            (r"{USENIX} Annual Technical Conference,", MatchType.CONTAINS),
            (r"$ATC$", MatchType.CONTAINS),
        },
        "CCPE": {
            (r"CCPE", MatchType.EXACT),  # not in DBPL, but just in case.
            (r"Concurrency - Practice and Experience", MatchType.EXACT),
            (r"Concurrency: practice and experience", MatchType.EXACT),
            (r"Concurrency and Computation: Practice and Experience", MatchType.EXACT),
        },
        # "TOIT": {
        #     "TOIT",
        #     "Transactions on Internet Technology",
        # },
        # "TWEB": {
        #     "TWEB",
        #     "Transactions on the Web"
        # },
        # "PODC": {
        #     "PODC",
        #     "Symposium on Principles of Distributed Computing",
        #
        # },
        # "Middleware": {
        #     "Middleware Conference",
        #     "International Middleware Conference",
        #     "International Conference on Distributed Systems Platforms"
        #     "Middleware",
        # },
        "ISC": {
            (r"ISC", MatchType.EXACT),
            (r"\{ISC\} (?!.*\bWorkshops\b)", MatchType.REGEX),
            (r"International Supercomputing Conference", MatchType.EXACT),
            (r"Supercomputer", MatchType.CONTAINS),
        },
        # "LISA": {
        #     "LISA",
        #     "Large Installation System Administration Conference",
        #     "Conference on Systems Administration",
        # },
        "FAST": {
            (r"FAST", MatchType.EXACT),
            (r"{FAST}", MatchType.CONTAINS),
            (r"$\{$FAST$\}$", MatchType.CONTAINS),
        },
        "SYSTOR": {
            (r"SYSTOR", MatchType.EXACT),
            (r"The Israeli Experimental Systems Conference", MatchType.CONTAINS),
            (r"International Conference on Systems and Storage(,|$)", MatchType.REGEX),
        },
        "INFOCOM": {
            (r"INFOCOM", MatchType.EXACT),
            (r"\{INFOCOM\}(?!.*\bWorkshops?\b).*$", MatchType.REGEX),
            (r"IEEE INFOCOM(?!.*\bWorkshops?\b).*$", MatchType.REGEX),
        },
        "CloudCom": {
            (r"^CloudCom( \(\d\))?$", MatchType.REGEX),  # DBLP
            (r"(CloudCom)", MatchType.CONTAINS),
            (r", CloudCom \d{4},", MatchType.REGEX),
            (r"International Conference on Cloud Computing Technology and Science, CloudCom", MatchType.CONTAINS),
        },
        "ICPP": {
            (r"^ICPP( \(\d\))?$", MatchType.REGEX),
            (r"International Conference on Parallel Processing(,|$)(?!.*\bWorkshop\b).*", MatchType.REGEX),
            (r"\{ICPP\}(?!.*\bWorkshop\b).*$", MatchType.REGEX),
        },
        "HPCC": {
            (r"HPCC", MatchType.EXACT),  # DBLP
            (r"{HPCC}", MatchType.CONTAINS),
            (r"HPCC-ICESS", MatchType.EXACT),
            (r"HPCC/CSS/ICESS", MatchType.EXACT),
            (r"HPCC/SmartCity/DSS", MatchType.EXACT),
            (r"HPCC/EUC", MatchType.EXACT),
            (r"^(?=.*\bInternational Conference on\b)(?=.*\bHigh Performance Computing and Communications?\b).*$",
             MatchType.REGEX),
        },
        "IJHPCA": {
            (r"^IJHPCA( \(\d\))?$", MatchType.REGEX),
            (r"{IJHPCA}", MatchType.CONTAINS),
            (r"International Journal of High Performance Computing Applications", MatchType.ENDS_WITH),
        },
        "e-Science": {
            (r"e-Science", MatchType.EXACT),  # used by DBLP
            (r"e-Science and Grid Computing,", MatchType.STARTS_WITH),
            (r"International Conference on e-Science, (?!eScience Workshops)", MatchType.REGEX),
            (r"International Conference on e-Science and Grid Technologies", MatchType.CONTAINS),
        },
        # "CIS": {
        #     "Computational Intelligence and Security"
        # },
        # "MIPRO": {
        #     "MIPRO",
        #     "Information and Communication Technology, Electronics and Microelectronics"
        # },
        "TOMPECS": {
            (r"TOMPECS", MatchType.EXACT),  # used by DBLP
            (r"{TOMPECS}", MatchType.EXACT),
            (r"Transactions on Modeling and Performance Evaluation of Computing Systems", MatchType.CONTAINS),
        },
        # "JISA": {
        #     "JISA",
        #     "Journal of Internet Services and Applications"
        # },
        # "NetGames": {
        #     "NetGames",
        #     "Annual Workshop on Network and Systems Support for Games"
        # },
        "PPOPP": {
            (r"PPOPP", MatchType.EXACT),
            (r"{PPEALS}", MatchType.CONTAINS),
            (r"(PPOPP)", MatchType.CONTAINS),
            (r"\{?ACM\}? \{?SIGPLAN\}? Symposium on Principles and Practice of Parallel Programming", MatchType.REGEX),
        },
        "TJS": {
            (r"TJS", MatchType.EXACT),
            (r"The Journal of Supercomputing", MatchType.EXACT),
        },
        "PC": {
            (r"PC", MatchType.EXACT),
            (r"Parallel Computing", MatchType.EXACT),
        },
        "HiPC": {
            (r"HiPC", MatchType.EXACT),
            (r"(HiPC)", MatchType.CONTAINS),
            (r"HiPC'\d{2}", MatchType.REGEX),
            (r"International Conference on High Performance Computing,", MatchType.CONTAINS),
        },
        "TC": {
            (r"TC", MatchType.EXACT),
            (r"{IEEE} Trans. Computers", MatchType.EXACT),
            (r"IEEE Transactions on Computers", MatchType.EXACT),
        },
        "PODS": {
            (r"PODS", MatchType.EXACT),  # DBLP
            (r"(S|s)ymposium on Principles of Database Systems", MatchType.REGEX),
        },
        "HotCloud": {
            (r"HotCloud", MatchType.EXACT),
            (r"Workshop on Hot Topics in Cloud Computing,", MatchType.CONTAINS),

        },
        "SPIRE": {
            (r"SPIRE", MatchType.EXACT),
            (r"{SPIRE}", MatchType.CONTAINS),
            (r"(i|I)nternational (s|S)ymposium on (s|S)tring (p|P)rocessing and (i|I)nformation (r|R)etrieval",
             MatchType.REGEX),
            (r"String Processing and Information Retrieval:", MatchType.CONTAINS),
        },
        "JIDPS": {
            (r"JIDPS", MatchType.EXACT),
            (r"Journal of Integrated Design and Process Science", MatchType.EXACT),
            (r"Transactions of the {SDPS}", MatchType.CONTAINS),
            (r"J. Integrated Design {\&} Process Science", MatchType.EXACT),
        },
        "DSN": {
            (r"DSN", MatchType.EXACT),
            (r"International Conference on Dependable Systems and Networks(?!.*\bWorkshops\b).*", MatchType.REGEX),
        },
        "SASO": {
            (r"SASO", MatchType.EXACT),
            (r"International Conference on Self-Adaptive and Self-Organizing Systems", MatchType.CONTAINS),
        },
    }

    def __init__(self):
        self.cache = dict()
        self.starts_with_dict = dict()
        self.ends_with_dict = dict()
        self.compiled_regexes = dict()
        self.contains_dict = dict()

        for venue_abbreviation, match_tuples in self.venues.items():
            regex_parts = []

            for match_line, matchtype in match_tuples:
                if matchtype == MatchType.REGEX:
                    regex_parts.append(match_line)

                elif matchtype == MatchType.EXACT:
                    self.cache[match_line] = venue_abbreviation

                elif matchtype == MatchType.STARTS_WITH:
                    if venue_abbreviation not in self.starts_with_dict:
                        self.starts_with_dict[venue_abbreviation] = []
                    self.starts_with_dict[venue_abbreviation].append(match_line)

                elif matchtype == MatchType.ENDS_WITH:
                    if venue_abbreviation not in self.ends_with_dict:
                        self.ends_with_dict[venue_abbreviation] = []
                    self.ends_with_dict[venue_abbreviation].append(match_line)

                elif matchtype == MatchType.CONTAINS:
                    if venue_abbreviation not in self.contains_dict:
                        self.contains_dict[venue_abbreviation] = []

                    self.contains_dict[venue_abbreviation].append(match_line)

            if len(regex_parts):
                # Concatenate regexes using OR groups to improve the speed. One giant regex evaluates faster than
                # multiple smaller ones.
                combined_regex = "({})".format("|".join(["({})".format(r) for r in regex_parts]))
                self.compiled_regexes[venue_abbreviation] = re.compile(combined_regex)

    def get_abbreviation(self, bibtex_string):
        if bibtex_string in self.cache:
            return self.cache[bibtex_string]

        for venue_abbreviation, strings in self.starts_with_dict.items():
            if any(str(bibtex_string).startswith(s) for s in strings):
                self.cache[bibtex_string] = venue_abbreviation
                return venue_abbreviation

        for venue_abbreviation, strings in self.ends_with_dict.items():
            if any(str(bibtex_string).endswith(s) for s in strings):
                self.cache[bibtex_string] = venue_abbreviation
                return venue_abbreviation

        for venue_abbreviation, contain_strings in self.contains_dict.items():
            if any(s in bibtex_string for s in contain_strings):
                self.cache[bibtex_string] = venue_abbreviation
                return venue_abbreviation

        for venue_abbreviation, regex in self.compiled_regexes.items():
            if regex.search(bibtex_string):
                self.cache[bibtex_string] = venue_abbreviation
                return venue_abbreviation

        return None
