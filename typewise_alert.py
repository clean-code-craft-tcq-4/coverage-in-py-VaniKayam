
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def passive_cooling(coolingType):
    if coolingType == 'PASSIVE_COOLING':
      lowerlimit = 0
      upperlimit = 45
      return lowerlimit,upperlimit
    return None

def hi_active_cooling(coolingType):
    if coolingType == 'HI_ACTIVE_COOLING':
      lowerlimit = 0
      upperlimit = 35
      return lowerlimit,upperlimit
    return None

def med_active_cooling(coolingType):
    if coolingType == 'MED_ACTIVE_COOLING':
        lowerlimit = 0
        upperlimit = 40
        return lowerlimit,upperlimit
    return None

def classify_temperature_breach(coolingType, temperatureInC):
    ftpr = [passive_cooling,hi_active_cooling,med_active_cooling]
    i=0
    while(i<3):
        limits= ftpr[i](coolingType)
        if(limits != None):
            return infer_breach(temperatureInC,limits[0],limits[1])
        i+=1
    return None

def is_alertcontroller(alertTarget,breachType):
    if(alertTarget == "TO_CONTROLLER"):
        send_to_controller(breachType)
        return 0
    return None
        
def is_alertemail(alertTarget,breachType):
    if(alertTarget == "TO_EMAIL"):
        send_to_email(breachType)
        return 0
    return None
        

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  ftpr = [is_alertcontroller,is_alertemail]
  i=0
  while(i<2):
      feedback = ftpr[i](alertTarget,breachType)
      if(feedback != None):
          break
      i+=1



def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
