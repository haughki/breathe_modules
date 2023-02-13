from commands.imports import *


Breathe.add_commands(
    context = AppContext(executable='MobaXterm'),
    mapping = {
        "Smitty super do": Text("sudo -u smdi -s") + Key("enter"),
        "direct dev": Text("cd /apps/user/cdd/dev") + Key("enter"),
        "direct registration dev": Text("cd /apps/user/cdd/dev/conda_envs/app_cdd_peptide_reg_dev/lib/python3.9/site-packages/cdd_peptide_reg") + Key("enter"),
        "direct conda dev": Text("cd /apps/user/cdd/dev/conda_envs/app_cdd_peptide_reg_dev") + Key("enter"),
        "direct config dev": Text("cd /apps/user/cdd/dev/conf/server/cddweb-dev") + Key("enter"),
        "direct logs dev": Text("cd /apps/user/cdd/dev/log/cdd_peptide_reg") + Key("enter"),
        "direct data loader files dev": Text("cd /gstore/scratch/smdd/app_cdd_peptide_reg/dev/data_loader_files") + Key("enter"),
        "activate conda dev": Text("conda activate app_cdd_peptide_reg_dev") + Key("enter"),
        "restart registration dev": Text("sudo supervisorctl restart cdd_peptide_reg:"),
        "deploy registration dev": Text("bash -i ./server_deploy.sh dev "),

        "direct prod": Text("cd /apps/user/cdd/prd") + Key("enter"),
        "direct registration prod": Text("cd /apps/user/cdd/prd/conda_envs/app_cdd_peptide_reg_prd/lib/python3.9/site-packages/cdd_peptide_reg") + Key("enter"),
        "direct conda prod": Text("cd /apps/user/cdd/prd/conda_envs/app_cdd_peptide_reg_prd") + Key("enter"),
        "direct config prod": Text("cd /apps/user/cdd/prd/conf/server/cddweb-prd") + Key("enter"),
        "direct logs prod": Text("cd /apps/user/cdd/prd/log/cdd_peptide_reg") + Key("enter"),
        "direct data loader files prod": Text("cd /gstore/scratch/smdd/app_cdd_peptide_reg/prd/data_loader_files") + Key("enter"),
        "activate conda prod": Text("conda activate app_cdd_peptide_reg_prd") + Key("enter"),
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
