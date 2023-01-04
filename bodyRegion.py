import pandas as pd
humanBody = {
    'head' : ["brain","mening","neur","cerebr","dental","cran","trigemin","mastoid","orbit","tons","amigd","adeno","mandible","catarac","nose","sinus","nasal","sphenoi","scleral","corneal","teeth","tooth","zygoma","ventriculoperitoneal","rhino","septoplasty","face","facial","trabeculec","vitrec","mastoi"],
    'neck' : ["trach","cervical","neck","esophagectomy","esophagostomy","carotid","thyroi","laryng","pharyng"],
    'thorax' : ["esophagectomy","bronch","thora"],
    'mediastinum' : ["cardiac","mediastin","heart","pace","pericar","cardio","atrial","STEMI","ablation","myotomy","thym","CV","ravitch","pectus","maze","stern","mitral", "tricusp","sternal","ICD","chest","CABG","aort","WATCHMAN","PCI" ],
    #9 abdominal regions - epigastric, L&R hypocondriac,umbilical, L&R flanks, hypogastric, L&R iliac regions
    'RHC' : ["hepatec","segmentec","liver","chole","bili","bile duct"],
    'EPI' : ["gast","Whipple","fundo","hiatal","esophag","panc","EGD","diaphragm"],
    'LHC' : ["splen"],
    'RF' : ["right kidney", "right neph","right adrenal"],
    'U' : ["small intestine","small bowel","enter","jejun","bowel","umbilical"],
    'LF' : ["left kidney", "left neph", "left adrenal"],
    'RIR' : ["append","right salping","right ooph","ileo"],
    'HYPO' : ["cyst","hyst","prost","proct","recta","uterus","myomec","colpo","rectopexy","urogra","sling","uroflow","intravesical"],
    'LIR' : ["sigm","left salping","left ooph","hartman"],
    ##
    'abdomen': ["laparo","abdom","stoma","retroperitone","INTESTINAL ADHESION", "adhesi","oment","peritone"],
    'orificial':["fistulotomy","fistulectomy","anal","hemorr","fissurec"],
    'genitalia': ["penis","penec","orchi","testic","epidi","vulv","circumcision","scrot","vagina","hydrocele","perineo","vasectomy"],
    #Double organs to be sorted
    'urinary': ["neph","kidney","renal","uret","pyelo","litho"], ## either RF or LF
    'femaleGenital': ["salping","ooph","col","ovary","adren","breast","mastec","masto"],
    'inguinalRegion'["inguinal"],
    'colon': ["colectomy"],
    'genHernia':["hernia"],
    'sidedThorax:["lung","lob"],
    #Superficial procedures
    'non-cavity': ["wound","subcut","closure", "biopsy","drain","wall","evacuation","extremity","block","dural","debridement","excision","absc","lipec","spinal","nerve","anesthesia","laminec"],
    #Skeleton image
    'ortho' : ["reduction","arthro","knee","tibia","hip","lumbar","shoulder","femur","amputation","tendon","carpal","elbow","foot","toe","fixation","clavic","vertebro","ankle","humerus","fasciotomy","joint","acetabulum","sacroili","thigh","wrist","ulna","osteo","bone","tendi","patela","trochant"],
    #Vessels image
    'vascular': ["cath","arter","veno","emboli","aort","fistula","IVC","varic","vein","bypass"],
    'implants': ["implant","explant","insertion","removal"]
    
    
}

df = pd.read_excel('Procedures.xlsx')
count = 0

def bodyRegion(check,output):
    
    for region,organs in humanBody.items():
        for organ in organs:
            if organ.lower() in str(check.lower()):
                if output == "matched":
                    print(region,check,organ)
                
                return
    if output == "unmatched":
        print("Error",check)
        global count
        count += 1
        
#def laterality(side):
# function to receive side input and output correct region    
        
for index, row in df.iterrows():
    bodyRegion(row['procedure_name'],"matched")
print("Total unmatched:",count)  
    
  



     

