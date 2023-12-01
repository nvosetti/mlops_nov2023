import yaml
import joblib
import os


params_path = "params.yaml"
schema_path = os.path.join("prediction_service", "schema_in.json")


class NotInRange(Exception) :
    def __init__(self, message="value not in given range - by Oracle India") :
        self.message = message
        super().__init__(self.message)


class NotInCols(Exception) :
    def __init__(self, message="Not in cols") :
        self.message = message
        super().__init__(self.message)

def read_params(config_path=params_path) :
    with open(config_path) as yaml_file :
        config = yaml.safe_load(yaml_file)
    return config

def predict(data) :
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data).tolist()[0]
    try :
        if 3 <= prediction <= 8 :
            return prediction
        else :
            raise NotInRange
    except NotInRange :
        return "Unexpected result"