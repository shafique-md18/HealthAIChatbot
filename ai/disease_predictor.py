from keras.models import load_model
from pandas import DataFrame
import copy
from .utils import getAbsPath

# create test for prediction
SYMPTOMS = {'itching': {0: 0}, 'skin_rash': {0: 0}, 'nodal_skin_eruptions': {0: 0}, 'continuous_sneezing': {0: 0}, 'shivering': {0: 0}, 'chills': {0: 0}, 'joint_pain': {0: 0}, 'stomach_pain': {0: 0}, 'acidity': {0: 0}, 'ulcers_on_tongue': {0: 0}, 'muscle_wasting': {0: 0}, 'vomiting': {0: 0}, 'burning_micturition': {0: 0}, 'spotting_ urination': {0: 0}, 'fatigue': {0: 0}, 'weight_gain': {0: 0}, 'anxiety': {0: 0}, 'cold_hands_and_feets': {0: 0}, 'mood_swings': {0: 0}, 'weight_loss': {0: 0}, 'restlessness': {0: 0}, 'lethargy': {0: 0}, 'patches_in_throat': {0: 0}, 'irregular_sugar_level': {0: 0}, 'cough': {0: 0}, 'high_fever': {0: 0}, 'sunken_eyes': {0: 0}, 'breathlessness': {0: 0}, 'sweating': {0: 0}, 'dehydration': {0: 0}, 'indigestion': {0: 0}, 'headache': {0: 0}, 'yellowish_skin': {0: 0}, 'dark_urine': {0: 0}, 'nausea': {0: 0}, 'loss_of_appetite': {0: 0}, 'pain_behind_the_eyes': {0: 0}, 'back_pain': {0: 0}, 'constipation': {0: 0}, 'abdominal_pain': {0: 0}, 'diarrhoea': {0: 0}, 'mild_fever': {0: 0}, 'yellow_urine': {0: 0}, 'yellowing_of_eyes': {0: 0}, 'acute_liver_failure': {0: 0}, 'fluid_overload': {0: 0}, 'swelling_of_stomach': {0: 0}, 'swelled_lymph_nodes': {0: 0}, 'malaise': {0: 0}, 'blurred_and_distorted_vision': {0: 0}, 'phlegm': {0: 0}, 'throat_irritation': {0: 0}, 'redness_of_eyes': {0: 0}, 'sinus_pressure': {0: 0}, 'runny_nose': {0: 0}, 'congestion': {0: 0}, 'chest_pain': {0: 0}, 'weakness_in_limbs': {0: 0}, 'fast_heart_rate': {0: 0}, 'pain_during_bowel_movements': {0: 0}, 'pain_in_anal_region': {0: 0}, 'bloody_stool': {0: 0}, 'irritation_in_anus': {0: 0}, 'neck_pain': {0: 0}, 'dizziness': {0: 0}, 'cramps': {0: 0}, 'bruising': {0: 0}, 'obesity': {0: 0}, 'swollen_legs': {0: 0}, 'swollen_blood_vessels': {0: 0}, 'puffy_face_and_eyes': {0: 0}, 'enlarged_thyroid': {0: 0}, 'brittle_nails': {0: 0}, 'swollen_extremeties': {0: 0}, 'excessive_hunger': {0: 0}, 'extra_marital_contacts': {0: 0}, 'drying_and_tingling_lips': {0: 0}, 'slurred_speech': {0: 0}, 'knee_pain': {0: 0}, 'hip_joint_pain': {0: 0}, 'muscle_weakness': {0: 0}, 'stiff_neck': {0: 0}, 'swelling_joints': {0: 0}, 'movement_stiffness': {0: 0}, 'spinning_movements': {0: 0}, 'loss_of_balance': {0: 0}, 'unsteadiness': {0: 0}, 'weakness_of_one_body_side': {0: 0}, 'loss_of_smell': {0: 0}, 'bladder_discomfort': {0: 0}, 'foul_smell_of urine': {0: 0}, 'continuous_feel_of_urine': {0: 0}, 'passage_of_gases': {0: 0}, 'internal_itching': {0: 0}, 'toxic_look_(typhos)': {0: 0}, 'depression': {0: 0}, 'irritability': {0: 0}, 'muscle_pain': {0: 0}, 'altered_sensorium': {0: 0}, 'red_spots_over_body': {0: 0}, 'belly_pain': {0: 0}, 'abnormal_menstruation': {0: 0}, 'dischromic _patches': {0: 0}, 'watering_from_eyes': {0: 0}, 'increased_appetite': {0: 0}, 'polyuria': {0: 0}, 'family_history': {0: 0}, 'mucoid_sputum': {0: 0}, 'rusty_sputum': {0: 0}, 'lack_of_concentration': {0: 0}, 'visual_disturbances': {0: 0}, 'receiving_blood_transfusion': {0: 0}, 'receiving_unsterile_injections': {0: 0}, 'coma': {0: 0}, 'stomach_bleeding': {0: 0}, 'distention_of_abdomen': {0: 0}, 'history_of_alcohol_consumption': {0: 0}, 'fluid_overload.1': {0: 0}, 'blood_in_sputum': {0: 0}, 'prominent_veins_on_calf': {0: 0}, 'palpitations': {0: 0}, 'painful_walking': {0: 0}, 'pus_filled_pimples': {0: 0}, 'blackheads': {0: 0}, 'scurring': {0: 0}, 'skin_peeling': {0: 0}, 'silver_like_dusting': {0: 0}, 'small_dents_in_nails': {0: 0}, 'inflammatory_nails': {0: 0}, 'blister': {0: 0}, 'red_sore_around_nose': {0: 0}, 'yellow_crust_ooze': {0: 0}}

LABELS = ['(vertigo) Paroymsal  Positional Vertigo', 'AIDS', 'Acne', 'Alcoholic hepatitis', 'Allergy', 'Arthritis', 'Bronchial Asthma', 'Cervical spondylosis', 'Chicken pox', 'Chronic cholestasis', 'Common Cold', 'Dengue', 'Diabetes ', 'Dimorphic hemmorhoids(piles)', 'Drug Reaction', 'Fungal infection', 'GERD', 'Gastroenteritis', 'Heart attack', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Hypertension ', 'Hyperthyroidism', 'Hypoglycemia', 'Hypothyroidism', 'Impetigo', 'Jaundice', 'Malaria', 'Migraine', 'Osteoarthristis', 'Paralysis (brain hemorrhage)', 'Peptic ulcer diseae', 'Pneumonia', 'Psoriasis', 'Tuberculosis', 'Typhoid', 'Urinary tract infection', 'Varicose veins', 'hepatitis A']

DISEASE_MODEL = load_model(getAbsPath('disease_model.h5'))

def get_symp_pd(symptoms_list):
    s_dict = copy.deepcopy(SYMPTOMS)
    for symp in symptoms_list:
        if symp in s_dict:
            s_dict.get(symp)[0] = 1
    # convert symptoms to pandas data frame
    s_dict = DataFrame(s_dict)
    
    return s_dict

def get_disease_name(symptoms_list):
    symptoms_list = get_symp_pd(symptoms_list)
    y_prob = DISEASE_MODEL.predict(symptoms_list) 
    y_classes = y_prob.argmax(axis=-1)
    
    return LABELS[y_prob[0].argmax(axis=-1)]

def get_disease_msg(msg):
    symp_list = list(msg.split(" "))
    return 'You might have ' + get_disease_name(symp_list)

def test():
    symp_disease = [
        [['itching', 'skin_rash'], ''],
        [['itching', 'skin_rash', 'fatigue'], ''],
        [['sweating', 'chest_pain'], ''],
        [['shivering', 'chills', 'watering_from_eyes'], ''],
        [['weight_loss', 'high_fever', 'yellowish_skin'], ''],
        [['skin_rash', 'chills', 'joint_pain', 'pain_behind_the_eyes', 'red_spots_over_body'], ''],
        [['skin_rash', 'pus_filled_pimples'], ''],
    ]

    for i in range(len(symp_disease)):
        if (len(symp_disease[i][0]) != 0):
            d_name = get_disease_name(symp_disease[i][0])
            print(d_name + ' : ' + str(symp_disease[i][0]))