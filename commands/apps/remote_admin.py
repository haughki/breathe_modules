from commands.imports import *

def tail_app_log(n=None):
    if n and n > 1:
        Text("tail -" + str(n) + " ./cdd_peptide_reg_app.log").execute()
        Key("enter").execute()
    else:
        Text("tail -f ./cdd_peptide_reg_app.log").execute()
        Key("enter").execute()

Breathe.add_commands(
    context = AppContext(executable='ubuntu') | AppContext(executable='MobaXterm') | AppContext(executable='mintty') | AppContext(executable='WindowsTerminal'),
    mapping = {
        "pepis super do": Text("sudo -u pepis -s") + Key("enter"),
        "sue doop": Text("sudop") + Key("enter"),
        "direct cdd": Text("cd /apps/user/gRED/cdd") + Key("enter"),

        "direct registration dev": Text("cd /apps/user/gRED/cdd/software/venvs/dev/cdd_peptide_reg_dev/lib/python3.11/site-packages/cdd_peptide_reg") + Key("enter"),
        "direct environment dev": Text("cd /apps/user/gRED/cdd/software/venvs/dev/cdd_peptide_reg_dev") + Key("enter"),
        "direct config dev": Text("cd /apps/user/gRED/cdd/software/dev/conf/server/sc1lvcddwebd01") + Key("enter"),
        "direct logs dev": Text("cd /gpfs/homefs/site/home/pepis/cdd_peptide_reg.resources/dev/log.files") + Key("enter"),
        "direct data loader files dev": Text("cd /gpfs/homefs/site/home/pepis/cdd_peptide_reg.resources/dev/log.files/data_loader_files") + Key("enter"),
        "direct certs dev": Text("cd /gpfs/homefs/site/home/pepis/.config/ssl/dev") + Key("enter"),
        "activate environment dev": Text("source /apps/user/gRED/cdd/software/venvs/dev/cdd_peptide_reg_dev/bin/activate") + Key("enter"),
        "restart registration dev": Text("supervisorctl restart cdd_peptide_reg:"),
        "stop registration dev": Text("supervisorctl stop cdd_peptide_reg:"),

        "direct registration prod": Text("cd /apps/user/gRED/cdd/software/venvs/prd/cdd_peptide_reg_prd/lib/python3.11/site-packages/cdd_peptide_reg") + Key("enter"),
        "direct environment prod": Text("cd /apps/user/gRED/cdd/software/venvs/prd/cdd_peptide_reg_prd") + Key("enter"),
        "direct config prod": Text("cd /apps/user/gRED/cdd/software/prd/conf/server/sc1lvcddwebp01") + Key("enter"),
        "direct logs prod": Text("cd /gpfs/homefs/site/home/pepis/cdd_peptide_reg.resources/prd/log.files") + Key("enter"),
        "direct data loader files prod": Text("cd /gpfs/homefs/site/home/pepis/cdd_peptide_reg.resources/prd/log.files/data_loader_files") + Key("enter"),
        "direct certs prod": Text("cd /gpfs/homefs/site/home/pepis/.config/ssl/prd") + Key("enter"),
        "activate environment prod": Text("source /apps/user/gRED/cdd/software/venvs/prd/cdd_peptide_reg_prd/bin/activate") + Key("enter"),
        "restart registration prod": Text("supervisorctl restart cdd_peptide_reg:"),
        "stop registration prod": Text("supervisorctl stop cdd_peptide_reg:"),

        "Smitty super do": Text("sudo -u smdi -s") + Key("enter"),
        # "direct dev": Text("cd /apps/user/cdd/dev") + Key("enter"),
        # "direct registration dev": Text("cd /apps/user/cdd/dev/conda_envs/app_cdd_peptide_reg_dev/lib/python3.11/site-packages/cdd_peptide_reg") + Key("enter"),
        # "direct environment dev": Text("cd /apps/user/cdd/dev/conda_envs/app_cdd_peptide_reg_dev") + Key("enter"),
        # "direct config dev": Text("cd /apps/user/cdd/dev/conf/server/cddweb-dev") + Key("enter"),
        # "direct logs dev": Text("cd /apps/user/cdd/dev/log/cdd_peptide_reg") + Key("enter"),
        # "direct data loader files dev": Text("cd /gstore/scratch/smdd/app_cdd_peptide_reg/dev/data_loader_files") + Key("enter"),
        # "direct extra dev": Text("cd /gstore/data/smdd/cdd/dev/cdd_peptide_reg") + Key("enter"),
        # "activate conda dev": Text("conda activate app_cdd_peptide_reg_dev") + Key("enter"),
        # "restart registration dev": Text("sudo supervisorctl restart cdd_peptide_reg:"),
        # "stop registration dev": Text("sudo supervisorctl stop cdd_peptide_reg:"),
        # "deploy registration dev": Text("bash -i ./server_deploy.sh dev "),

        # "direct prod": Text("cd /apps/user/cdd/prd") + Key("enter"),
        # "direct registration prod": Text("cd /apps/user/cdd/prd/conda_envs/app_cdd_peptide_reg_prd/lib/python3.11/site-packages/cdd_peptide_reg") + Key("enter"),
        # "direct environment prod": Text("cd /apps/user/cdd/prd/conda_envs/app_cdd_peptide_reg_prd") + Key("enter"),
        # "direct config prod": Text("cd /apps/user/cdd/prd/conf/server/cddweb-prd") + Key("enter"),
        # "direct logs prod": Text("cd /apps/user/cdd/prd/log/cdd_peptide_reg") + Key("enter"),
        # "direct data loader files prod": Text("cd /gstore/scratch/smdd/app_cdd_peptide_reg/prd/data_loader_files") + Key("enter"),
        # "direct extra prod": Text("cd /gstore/data/smdd/cdd/prd/cdd_peptide_reg") + Key("enter"),
        # "activate conda prod": Text("conda activate app_cdd_peptide_reg_prd") + Key("enter"),

        "direct (aestel | Aestel) dev": Text("cd /apps/user/cdd/dev/Aestel/config/dataLoader/partner_data/genentech/peptide") + Key("enter"),
        "direct (aestel | Aestel) prod": Text("cd /apps/user/cdd/prd/Aestel/config/dataLoader/partner_data/genentech/peptide") + Key("enter"),

        "tail app log [<n>]": Function(tail_app_log),

        # general commands
        "supervisor status": Text("supervisorctl status "),
        "supervisor stop": Text("supervisorctl stop "),
        "supervisor start": Text("supervisorctl start "),
        "supervisor restart": Text("supervisorctl restart "),
    },

    extras = [
        Integer("t", 1, 50),
        Dictation("text"),
        Dictation("text2"),
        IntegerRef("n", 1, 50000),
        Integer("w", 0, 10),
        Integer("x", 0, 10),
        Integer("y", 0, 10),
        Integer("z", 0, 10)
    ],
    defaults = {
        "t": 1,
        "text": "",
        "text2": ""
    }
)
