import pandas as pd
humanBody = {
    'special cases' : ["colectomy","hernia"],
    'head' : ["brain","mening","neur","cerebr","dental","cran","trigemin","mastoid","orbit","tons","amigd","adeno","mandible","catarac","nose","sinus","nasal","sphenoi","scleral","corneal","teeth","tooth","zygoma","VENTRICULOPERITONEAL","rhino","septoplasty","face","facial","trabeculec"],
    'neck' : ["trach","cervical","neck","esophagectomy","esophagostomy","carotid","thyroi","laryng","pharing"],
    'thorax' : ["lung","lob","esophagectomy","bronch","thora"],
    'mediastinum' : ["cardiac","mediastin","heart","pace","pericar","cardio","atrial","STEMI","ablation","myotomy","thym","CV","ravitch","pectus","maze","stern","mitral", "tricusp","sternal","ICD","chest","CABG","aort","WATCHMAN","PCI" ],
    'RHC' : ["hepatec","segmentec","liver","chole","bili","bile duct"],
    'EPI' : ["gast","Whipple","fundo","hiatal","esophag","panc","EGD","diaphragm"],
    'LHC' : ["splen"],
    'RF' : ["right kidney", "right neph","right adrenal"],
    'U' : ["small intestine","small bowel","enter","jejun","bowel"],
    'LF' : ["left kidney", "left neph", "left adrenal"],
    'RIR' : ["append","right salping","right ooph","ileo"],
    'HIPO' : ["cyst","hyst","prost","proct","recta","uterus","myomec"],
    'LIR' : ["sigm","left salping","left ooph","hartman"],
    'abdomen': ["laparo","abdom","stoma","retroperitone","INTESTINAL ADHESION", "adhesi","oment","peritone"],
    'doubleOrgan:': ["neph","kidney","renal","salping","ooph","col","uret","ovary","adren","breast","litho","mastec","pyelo","masto"],
    'non-cavity': ["wound","hernia","subcut","closure", "biopsy","drain","wall","evacuation","extremity","anal","hemorrh","block","dural","debridement","excision","absc","lipec","spinal","fistulotomy","fistulectomy","nerve","anesthesia","laminec"],
    'ortho' : ["reduction","arthro","knee","tibia","hip","lumbar","shoulder","femur","amputation","tendon","carpal","elbow","foot","toe","fixation","clavic","vertebro","ankle","humerus","fasciotomy","joint","acetabulum","sacroili","thigh","wrist","ulna","osteo","bone","tendi","patela","trochant"],
    'vascular': ["cath","arter","veno","emboli","aort","fistula","IVC","varic","vein","bypass"],
    'genitalia': ["penis","penec","orchi","testic","epidi","vulv","circumcision","scrot","vagina","hydrocele","perineo"],
    'implants': ["implant","explant","insertion","removal"]
    
    
}
found = False
df = pd.read_excel('procedures.xlsx')
count = 0

def bodyRegion(check):
    for region,organs in humanBody.items():
        for organ in organs:
            if organ.lower() in str(check.lower()):
                print(region,check,organ)
                return
    ##print("Error",check)
    global count
    count += 1
    
for index, row in df.iterrows():
    bodyRegion(row['procedure_name'])

##print(count)
        
                
              
    

