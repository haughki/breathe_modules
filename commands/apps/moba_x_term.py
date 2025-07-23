from commands.imports import *

def tail_app_log(n=None):
    if n > 1:
        Text("tail -" + str(n) + " ./cdd_peptide_reg_app.log").execute()
        Key("enter").execute()
    else:
        Text("tail -f ./cdd_peptide_reg_app.log").execute()
        Key("enter").execute()

Breathe.add_commands(
    context = AppContext(executable='MobaXterm'),
    mapping = {
        "Smitty super do": Text("sudo -u smdi -s") + Key("enter"),
        "direct dev": Text("cd /apps/user/cdd/dev") + Key("enter"),
        "direct registration dev": Text("cd /apps/user/cdd/dev/conda_envs/app_cdd_peptide_reg_dev/lib/python3.11/site-packages/cdd_peptide_reg") + Key("enter"),
        "direct conda dev": Text("cd /apps/user/cdd/dev/conda_envs/app_cdd_peptide_reg_dev") + Key("enter"),
        "direct config dev": Text("cd /apps/user/cdd/dev/conf/server/cddweb-dev") + Key("enter"),
        "direct logs dev": Text("cd /apps/user/cdd/dev/log/cdd_peptide_reg") + Key("enter"),
        "direct data loader files dev": Text("cd /gstore/scratch/smdd/app_cdd_peptide_reg/dev/data_loader_files") + Key("enter"),
        "direct extra dev": Text("cd /gstore/data/smdd/cdd/dev/cdd_peptide_reg") + Key("enter"),
        "direct (aestel | Aestel) dev": Text("cd /apps/user/cdd/dev/Aestel/config/dataLoader/partner_data/genentech/peptide") + Key("enter"),
        "activate conda dev": Text("conda activate app_cdd_peptide_reg_dev") + Key("enter"),
        "restart registration dev": Text("sudo supervisorctl restart cdd_peptide_reg:"),
        "stop registration dev": Text("sudo supervisorctl stop cdd_peptide_reg:"),
        "deploy registration dev": Text("bash -i ./server_deploy.sh dev "),

        "direct prod": Text("cd /apps/user/cdd/prd") + Key("enter"),
        "direct registration prod": Text("cd /apps/user/cdd/prd/conda_envs/app_cdd_peptide_reg_prd/lib/python3.11/site-packages/cdd_peptide_reg") + Key("enter"),
        "direct conda prod": Text("cd /apps/user/cdd/prd/conda_envs/app_cdd_peptide_reg_prd") + Key("enter"),
        "direct config prod": Text("cd /apps/user/cdd/prd/conf/server/cddweb-prd") + Key("enter"),
        "direct logs prod": Text("cd /apps/user/cdd/prd/log/cdd_peptide_reg") + Key("enter"),
        "direct data loader files prod": Text("cd /gstore/scratch/smdd/app_cdd_peptide_reg/prd/data_loader_files") + Key("enter"),
        "direct extra prod": Text("cd /gstore/data/smdd/cdd/prd/cdd_peptide_reg") + Key("enter"),
        "direct (aestel | Aestel) prod": Text("cd /apps/user/cdd/prd/Aestel/config/dataLoader/partner_data/genentech/peptide") + Key("enter"),
        "activate conda prod": Text("conda activate app_cdd_peptide_reg_prd") + Key("enter"),

        "tail app log [<n>]": Function(tail_app_log),
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
