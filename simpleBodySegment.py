import pandas as pd

humanBody = {
    #Posterior
    'lumbar': ["neph","kidney","renal","uret","litho","adren"],
    'orificial':["fistulotomy","fistulectomy","anal","hemorr","fissurec","anal","hemorrh","anorectal"],
    'spinal': ["spine","laminec","vertebro"], #Height check
    #Anterior
    'special cases' : ["hernia","esophagectomy","clavicle","scapula"],
    'head' : ["brain","mening","neur","cerebr","dental","cran","trigemin","mastoid","orbit","tons","amigd","adeno","mandible","catarac","nose","sinus","nasal","sphenoi","scleral","corneal","teeth","tooth","zygoma","VENTRICULOPERITONEAL","rhino","septoplasty","face","facial","trabeculec"],
    'neck' : ["trach","cervical","neck","esophagostomy","carotid","thyroi","laryng","pharing"],
    'thorax' : ["lung","bronch","thora","cardiac","mediastin","heart","pace","pericar","cardio","atrial","STEMI","ablation","myotomy","thym","CV","ravitch","pectus","maze","stern","mitral", "tricusp","sternal","ICD","chest","CABG","aort","WATCHMAN","PCI","breast","mastec","masto", "ascending aorta"],
    'RUQ' : ["hepatec","liver","chole","bili","bile duct", "hepatic cyst"], #No side check
    'LUQ' : ["splen","spleen","gast","fundo","hiatal","esophag","EGD"], #No side check
    'RLQ' : ["append","ileo"], #No side check
    'LLQ' : ["sigm","hartman"], #No side check
    'upperA' : ["Whipple","panc","diaphragm","fren"],
    'lowerA' : ["salping","ooph","ovary","cyst","hyst","prost","proct","recta","uterus","myomec","pelvic","ilium","ischi","pubic"],
    'abdomen': ["laparo","abdom","stoma","retroperitone","adhesi","oment","peritone","small intestine","small bowel","enter","jejun","bowel","colectomy","colostomy"],
    'genitalia': ["penis","penec","orchi","testic","epidi","vulv","circumcision","scrot","vagina","hydrocele","perineo"],
    #Ortho & Vascular
    'upperLimb' :["shoulder","humer","bicep","tricep","brachial","elbow","radial","ulna","wrist","carpal","hand","digit","arm"],
    'lowerLimb' :["hip","acetabulum","femur","femoral","trochan","thigh","quadriceps","knee","patella","tibia","fibula","ankle","pedis","foot","feet","achiles","calcaneus","talus","toe","thumb","bunion","leg"], 
      
}

levels = ['cervic','thora','lumbar','sacr']

images = {
    "bilat":['head','neck','thorax','upperA','lowerA','abdomen','genitalia','upperLimb','lowerLimb'],
    "left":['l_head','l_neck','l_thorax','l_upperA','l_lowerA','l_abdomen','l_genitalia','l_upperLimb','l_lowerLimb'],
    "right": ['r_head','r_neck','r_thorax','r_upperA','r_lowerA','r_abdomen','r_genitalia','r_upperLimb','r_lowerLimb'],
}

df = pd.read_excel('procedureLaterality.xlsx')
def bodyRegion(check):
    for region,organs in humanBody.items():
        for organ in organs:
            if organ.lower() in str(check.lower()):
                if region == "lumbar" or region == "orificial":
                    print("Surgery is ",check,"|View is posterior | Site is",region,"|Side is",row['laterality'],"|Match is ",organ)
                    return
                elif region =="spinal":
                    spinalLevel = []
                    for height in levels:
                        if height in str(check.lower()):
                            spinalLevel.append(height)
                        
                    print("Surgery is ",check,"|View is posterior | Site is",region,"|Side is",row['laterality'],"|Height is ",spinalLevel,"|Match is ",organ)
                    return                                         
                else:
                    print("Surgery is ",check,"| View is anterior | Site is",region,"| Side is",row['laterality'],"|Match is ",organ)
                    return                

    
for index, row in df.iterrows():
    bodyRegion(row['proc_array'])
