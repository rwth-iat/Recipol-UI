from defusedxml.ElementTree import parse

from pathlib import Path

# Path
current_dir = Path(__file__).resolve().parent

TESTMTP1 = current_dir / "Artifact" / "HC10_2025-04-25.aml"
TESTMTP2 = current_dir / "Artifact" / "HC20HC40_2025-05-07.aml"
# TESTMTP2 = current_dir / "Artifact" / "test.aml"


### static variables
# TESTMTP1 = r"Artifact\HC10_2025-04-25.aml"
# TESTMTP2 = r"Artifact\HC20HC40_2025-05-07.aml"
#TESTMTP3 = r"Artefakte\HC30_manifest_new.aml"
TESTMTPS = [TESTMTP1, TESTMTP2]
NAMESPACE = "{http://www.dke.de/CAEX}"

### classes
class Instance:
    def __init__(self, name, id):
        self.name = name # name of the instance
        self.id = id # ID of the instance
        self.refid = None # refID of the instance
        self.min = None # minimal value of the instance
        self.max = None # maximal value of the instance
        self.default = None # default value of the instance
        self.unit = None # unit of the instance
        self.unitval: int = None # numerical identifier of the unit of the instance
        self.paramElem = {'WQC': {'Type': 'BYTE', 'ID': None, 'Default': None},
                          'OSLevel': {'Type': 'BYTE', 'ID': None, 'Default': None},
                          'CommandInfo': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'CommandOp': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'CommandInt': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'CommandExt': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'ProcedureOp': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'ProcedureInt': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'ProcedureExt': {'Type': 'BYTE', 'ID': None, 'Default': None},
                          'StateCur': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'CommandEn': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'ProcedureCur': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'ProcedureReq': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'Pos': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'PosTextID': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'InteractQuestionID': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'InteractAnswerID': {'Type': 'DWORD', 'ID': None, 'Default': None},
                          'InteractAddInfo': {'Type': 'STRING', 'ID': None, 'Default': None},
                          'OSLevel': {'Type': 'BYTE', 'ID': None, 'Default': None},
                          'ApplyEn': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ApplyExt': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ApplyOp': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ApplyInt': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'Sync': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateChannel': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateOffAut': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateOpAut': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateAutAut': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateOffOp': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateOpOp': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateAutOp': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateOpAct': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateAutAct': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'StateOffAct': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'SrcChannel': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'SrcExtAut': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'SrcIntAut': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'SrcIntOp': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'SrcExtOp': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'SrcIntAct': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'SrcExtAct': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ProcParamApplyEn': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ProcParamApplyExt': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ProcParamApplyOp': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ProcParamApplyInt': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ConfigParamApplyEn': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ConfigParamApplyExt': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ConfigParamApplyOp': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ConfigParamApplyInt': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'ReportValueFreeze': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'Ctrl': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'FwdCtrl': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'RevCtrl': {'Type': 'BOOL', 'ID': None, 'Default': None},
                          'V': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VExt': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VOp': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VInt': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VReq': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VOut': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VFbk': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VSclMin': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VSclMax': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VUnit': {'Type': 'INT', 'ID': None, 'Default': None},
                          'VMin': {'Type': 'REAL', 'ID': None, 'Default': None},
                          'VMax': {'Type': 'REAL', 'ID': None, 'Default': None}}

    def __str__(self):
        descr = f"NAME: {self.name}, ID={self.id}"
        descr += f"\n    Min: {self.min}, Max: {self.max}, Unit: {self.unit}"
        return descr

    def addRefId(self, refId: str):
        """Adds a refID to the instance"""
        self.refid = refId

    def addMin(self, minVal:float):
        """Adds a low limit value"""
        self.min = minVal

    def addMax(self, maxVal:float):
        """Adds a high limit value"""
        self.max = maxVal

    def addUnit(self, unit:str):
        """Adds a unit"""
        self.unit = unit

    def getName(self) -> str:
        """Returns the name of the instance"""
        return self.name

class Procedure:
    def __init__(self, name:str, id:str):
        self.name = name # name of the procedure
        self.id = id # id of the procedure
        self.params = [] # list of parameters of the procedure
        self.compl = None # flag that says if procedure is self completing or not
        self.procId = None # procedure ID
        self.serviceId = None # id of the service the procedure is under

    def __str__(self):
        descr = f"NAME: {self.name}, ID: {self.id}"
        descr += f"\n   Parameter: {self.params}"
        descr += f"\n   Self Completing: {self.compl}"
        return descr

    def addParameter(self, param:Instance) -> None:
        """Adds a parameter to the procedure"""
        self.params.append(param)

    def getParameter(self, id:str) -> Instance:
        """Returns the specified parameter"""
        for p in self.params:
            if p.id == id:
                return p

        return None

    def setSelfCompleting(self, complFlag:bool) -> None:
        """Sets the self completing flag of the procedure"""
        self.compl = complFlag

class Service:
    def __init__(self):
        self.name = "" # name of the service
        self.id = "" # id of the service
        self.refid = "" # refid of the service
        self.paramElem = {} # param elems of the service
        self.procs = [] # the procedures under the service

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, RefID: {self.refid}\nparamElem: {self.paramElem}\nProcedures: {self.procs}"

class Port:
    def __init__(self):
        self.name:str = "" # name of the port
        self.x:int = 0 # x coordinate of the port
        self.y:int = 0 # y coordinate of the port
        self.connectId = "" # ID of the connector of the port

class VisualObject:
    def __init__(self):
        self.name:str = "" # name of the visual object
        self.refId:str = "" # refId of the visual object
        self.refInst:Instance = None # the instance the visual object represents
        self.width:int = 0 # width of the visual object
        self.height:int = 0 # height of the visual object
        self.x:int = 0 # x coordinate of the visual object
        self.y:int = 0 # y coordinate of the visual object
        self.zindex:int = 0 # zindex of the visual object
        self.rotation:int = 0 # rotation of the visual object
        self.eClassVer:str = "" # eClass Version of the visual object
        self.eClassClass:str = "" # eClass Classification Class of the visual object
        self.eClassIRDI:str = "" # eClass IRDI of the visual object
        self.ports:list[Port] = [] # list of ports the visual object has

class Junction:
    def __init__(self):
        self.name:str = "" # name of the topology object
        self.x:int = 0 # x coordinate of the topology object
        self.y:int = 0 # y coordinate of the topology object
        self.zindex:int = 0 # z index of the topology object
        self.ports:list[Port] = [] # list of ports the topology object has

class Source:
    def __init__(self):
        self.name:str = "" # name of the source object
        self.x:int = 0 # x coordinate of the source object
        self.y:int = 0 # y coordinate of the source object
        self.termId:str = "" # term ID of the source object
        self.zindex:int = 0 # z index of the source object
        self.ports:list[Port] = [] # list of ports the source object has

class Sink:
    def __init__(self):
        self.name:str = "" # name of the sink object
        self.x:int = 0 # x coordinate of the sink object
        self.y:int = 0 # y coordinate of the sink object
        self.termId:str = "" # term ID of the sink object
        self.zindex:int = 0 # z index of the sink object
        self.ports:list[Port] = [] # list of ports the sink object has

class Pipe:
    def __init__(self):
        self.name:str = "" # name of the pipe
        self.direct:bool = False # whether the pipe is directed or not
        self.ep:str = "" # the edge path of the pipe
        self.zindex:int = 0 # the z index of the pipe
        self.ports:list[Port] = [] # list of ports of the pipe

class Line:
    def __init__(self):
        self.type:str = "" # the type of the line, either Function or Measurement
        self.name:str = "" # name of the line
        self.ep:str = "" # the edge path of the line
        self.zindex:int = 0 # the z index of the line
        self.ports:list[Port] = [] # list of ports of the line

class HMI:
    def __init__(self):
        self.type:str = "" # type of the HMI instance, either 'Service' or 'RI'
        self.width:int = 0 # width of the HMI instance
        self.height:int = 0 # height of the HMI instance
        self.hierarchy:str = "" # hierarchy level of the HMI instance
        self.visuals:list[VisualObject] = [] # list of visual objects of the HMI instance
        self.juncts:list[Junction] = [] # list of junction objects of the HMI instance
        self.srcs:list[Source] = [] # list of source objects of the HMI instance
        self.sinks:list[Sink] = [] # list of sink objects of the HMI instance
        self.pipes:list[Pipe] = [] # list of pipes of the HMI instance
        self.lines:list[Line] = [] # list of function lines of the HMI instance
        self.links:list[tuple[str,str]] = [] # list of internal links consisting of the refIds of both connection sides

class Pea:
    def __init__(self):
        self.name = "" # name of the mtp
        self.insts:list[Instance] = [] # list of instances
        self.sensacts = [] # list of sensors and actuators
        self.procs = [] # list of procedures
        self.servs = [] # list of services
        self.url = "" # address of the opc ua server
        self.ns = "" # namespace of the opc ua server
        self.nsid = None # index of the opc namespace
        self.hmis:list[HMI] = [] # list of the hmi representation(s) of the PEA

    def __str__(self):
        descr = f"{self.name}\nInstances:"
        for i in self.insts:
            descr += f"\n    {i}"
        descr += f"\nServices:"
        for p in self.servs:
            descr += f"\n   {p}"
        return descr

    def nameMtp(self, name:str) -> None:
        """Adds a name to the mtp"""
        self.name = name

    def addInstance(self, inst:Instance) -> None:
        """Adds an instance to the mtp"""
        self.insts.append(inst)

    def hasInstance(self, instId:str) -> bool:
        """Returns true if an instance with the given id exists, otherwise false"""
        for i in self.insts:
            if i.id == instId or i.refid == instId:
                return True

        return False

    def getInstance(self, instId:str) -> Instance:
        """Returns the instance with the given id"""
        for i in self.insts:
            if i.id == instId or i.refid == instId:
                return i

        return None

    def getInstanceByName(self, instName:str) -> Instance:
        """Returns the instance with the given name"""
        for i in self.insts:
            if i.name == instName:
                return i
        
        return None

    def addService(self, serv:Service) -> None:
        """Adds a procedure to the mtp."""
        self.servs.append(serv)

    def hasService(self, servId:str) -> bool:
        """Returns true if the mtp has the corresponding service."""
        for s in self.servs:
            if s.id == servId or s.refid == servId:
                return True
        return False

    def addUrl(self, url:str) -> None:
        """Adds an opc ua server url to the mtp"""
        self.url = url

    def getUrl(self) -> str:
        """Returns the url of the opc ua server"""
        return self.url

    def getService(self, id:str) -> Service:
        """Returns the service with the specified id"""
        for s in self.servs:
            if s.id == id:
                return s

        return None

    def getProcedure(self, procId:str) -> Procedure:
        """Returns the procedure with the specified id"""
        for p in self.procs:
            if p.id == procId:
                return p
        return None

    def hasProcedure(self, procId:str) -> bool:
        """Returns true if mtp has specified procedure."""
        for p in self.procs:
            if p.id == procId:
                return True
        return False

    def hasParameter(self, paramId:str) -> bool:
        """Returns true if there is a parameter with the specified id."""
        for p in self.procs:
            for param in p.params:
                if param.id == paramId:
                    return True
        return False

### functions
def getUnit(unitNr: int) -> str:
    """Returns the unit corresponding to the identifier"""
    match unitNr:
        case 1000:
            return "Kelvin"
        case 1001:
            return "Degree Celsius"
        case 1002:
            return "Degree Fahrenheit"
        case 1003:
            return "Degree Rankine"
        case 1004:
            return "Radian"
        case 1005:
            return "Degree"
        case 1006:
            return "Minute"
        case 1007:
            return "Second"
        case 1008:
            return "Gon"
        case 1009:
            return "Revolution"
        case 1010:
            return "Meter"
        case 1011:
            return "Kilometer"
        case 1012:
            return "Centimeter"
        case 1013:
            return "Millimeter"
        case 1014:
            return "Micrometer"
        case 1015:
            return "Nanometer"
        case 1016:
            return "Picometer"
        case 1017:
            return "Angstrom"
        case 1018:
            return "Foot"
        case 1019:
            return "Inch"
        case 1020:
            return "Yard"
        case 1021:
            return "Mile"
        case 1022:
            return "Nautical mile"
        case 1023:
            return "Square meter"
        case 1024:
            return "Square kilometer"
        case 1025:
            return "Square centimeter"
        case 1026:
            return "Square decimeter"
        case 1027:
            return "Square millimeter"
        case 1028:
            return "Are"
        case 1029:
            return "Hectare"
        case 1030:
            return "Square inch"
        case 1031:
            return "Square foot"
        case 1032:
            return "Square yard"
        case 1033:
            return "Square mile"
        case 1034:
            return "Cubic meter"
        case 1035:
            return "Cubic decimeter"
        case 1036:
            return "Cubic centimeter"
        case 1037:
            return "Cubic millimeter"
        case 1038:
            return "Liter"
        case 1039:
            return "Centiliter"
        case 1040:
            return "Milliliter"
        case 1041:
            return "Hectoliter"
        case 1042:
            return "Cubic inch"
        case 1043:
            return "Cubic foot"
        case 1044:
            return "Cubic yard"
        case 1045:
            return "Cubic mile"
        case 1046:
            return "Pint"
        case 1047:
            return "Quart"
        case 1048:
            return "US gallon"
        case 1049:
            return "Imperial gallon"
        case 1050:
            return "Bushel"
        case 1051:
            return "Barrel"
        case 1052:
            return "Barrel (liquid)"
        case 1053:
            return "Standard cubic foot"
        case 1054:
            return "Second"
        case 1055:
            return "Kilosecond"
        case 1056:
            return "Millisecond"
        case 1057:
            return "Microsecond"
        case 1058:
            return "Minute"
        case 1059:
            return "Hour"
        case 1060:
            return "Day"
        case 1061:
            return "Meter per second"
        case 1062:
            return "Millimeter per second"
        case 1063:
            return "Meter per hour"
        case 1064:
            return "Kilometer per hour"
        case 1065:
            return "Knot"
        case 1066:
            return "Inch per second"
        case 1067:
            return "Foot per second"
        case 1068:
            return "Yard per second"
        case 1069:
            return "Inch per minute"
        case 1070:
            return "Foot per minute"
        case 1071:
            return "Yard per minute"
        case 1072:
            return "Inch per hour"
        case 1073:
            return "Foot per hour"
        case 1074:
            return "Yard per hour"
        case 1075:
            return "Miles per hour"
        case 1076:
            return "Meter per square second"
        case 1077:
            return "Hertz"
        case 1078:
            return "Terahertz"
        case 1079:
            return "Gigahertz"
        case 1080:
            return "Megahertz"
        case 1081:
            return "Kilohertz"
        case 1082:
            return "Per second"
        case 1083:
            return "Per minute"
        case 1084:
            return "Revolutions per second"
        case 1085:
            return "Revolutions per minute"
        case 1086:
            return "Radian per second"
        case 1087:
            return "Per square second"
        case 1088:
            return "Kilogram"
        case 1089:
            return "Gram"
        case 1090:
            return "Milligram"
        case 1091:
            return "Megagram"
        case 1092:
            return "Metric ton"
        case 1093:
            return "Ounce"
        case 1094:
            return "Pound"
        case 1095:
            return "US ton"
        case 1096:
            return "British ton"
        case 1097:
            return "Kilogram per cubic meter"
        case 1098:
            return "Megagram per cubic meter"
        case 1099:
            return "Kilogram per cubic decimeter"
        case 1100:
            return "Gram per cubic centimeter"
        case 1101:
            return "Gram per cubic meter"
        case 1102:
            return "Metric ton per cubic meter"
        case 1103:
            return "Kilogram per liter"
        case 1104:
            return "Gram per milliliter"
        case 1105:
            return "Gram per liter"
        case 1106:
            return "Pound per cubic inch"
        case 1107:
            return "Pound per cubic foot"
        case 1108:
            return "Pound per US gallon"
        case 1109:
            return "US ton per cubic yard"
        case 1110:
            return "Degree Twaddell"
        case 1111:
            return "Degree Baumé (heavy)"
        case 1112:
            return "Degree Baumé (light)"
        case 1113:
            return "Degree API"
        case 1114:
            return "Specific gravity units"
        case 1115:
            return "Kilogram per meter"
        case 1116:
            return "Milligram per meter"
        case 1117:
            return "Tex"
        case 1118:
            return "Kilogram meter squared"
        case 1119:
            return "Kilogram meter per second"
        case 1120:
            return "Newton"
        case 1121:
            return "Meganewton"
        case 1122:
            return "Kilonewton"
        case 1123:
            return "Millinewton"
        case 1124:
            return "Micronewton"
        case 1125:
            return "Kilogram meter squared per second"
        case 1126:
            return "Newton meter"
        case 1127:
            return "Meganewton meter"
        case 1128:
            return "Kilonewton meter"
        case 1129:
            return "Millinewton meter"
        case 1130:
            return "Pascal"
        case 1131:
            return "Gigapascal"
        case 1132:
            return "Megapascal"
        case 1133:
            return "Kilopascal"
        case 1134:
            return "Millipascal"
        case 1135:
            return "Micropascal"
        case 1136:
            return "Hectopascal"
        case 1137:
            return "Bar"
        case 1138:
            return "Millibar"
        case 1139:
            return "Torr"
        case 1140:
            return "Atmosphere"
        case 1141:
            return "Pound per square inch"
        case 1142:
            return "Pound per square inch (absolute)"
        case 1143:
            return "Pound per square inch (gauge)"
        case 1144:
            return "Gram per square centimeter"
        case 1145:
            return "Kilogram per square centimeter"
        case 1146:
            return "Inch water column"
        case 1147:
            return "Inch water column at 4°C"
        case 1148:
            return "Inch water column at 68°F"
        case 1149:
            return "Millimeter water column"
        case 1150:
            return "Millimeter water column at 4°C"
        case 1151:
            return "Millimeter water column at 68°F"
        case 1152:
            return "Foot water column"
        case 1153:
            return "Foot water column at 4°C"
        case 1154:
            return "Foot water column at 68°F"
        case 1155:
            return "Inch mercury"
        case 1156:
            return "Inch mercury at 0°C"
        case 1157:
            return "Millimeter mercury"
        case 1158:
            return "Millimeter mercury at 0°C"
        case 1159:
            return "Pascal second"
        case 1160:
            return "Square meter per second"
        case 1161:
            return "Poise"
        case 1162:
            return "Centipoise"
        case 1163:
            return "Stokes"
        case 1164:
            return "Centistokes"
        case 1165:
            return "Newton per meter"
        case 1166:
            return "Millinewton per meter"
        case 1167:
            return "Joule"
        case 1168:
            return "Exajoule"
        case 1169:
            return "Petajoule"
        case 1170:
            return "Terajoule"
        case 1171:
            return "Gigajoule"
        case 1172:
            return "Megajoule"
        case 1173:
            return "Kilojoule"
        case 1174:
            return "Millijoule"
        case 1175:
            return "Watt hour"
        case 1176:
            return "Terawatt hour"
        case 1177:
            return "Gigawatt hour"
        case 1178:
            return "Megawatt hour"
        case 1179:
            return "Kilowatt hour"
        case 1180:
            return "Calorie (thermochemical)"
        case 1181:
            return "Kilocalorie (thermochemical)"
        case 1182:
            return "Megacalorie (thermochemical)"
        case 1183:
            return "British thermal unit"
        case 1184:
            return "Decatherm"
        case 1185:
            return "Foot-pound"
        case 1186:
            return "Watt"
        case 1187:
            return "Terawatt"
        case 1188:
            return "Gigawatt"
        case 1189:
            return "Megawatt"
        case 1190:
            return "Kilowatt"
        case 1191:
            return "Milliwatt"
        case 1192:
            return "Microwatt"
        case 1193:
            return "Nanowatt"
        case 1194:
            return "Picowatt"
        case 1195:
            return "Megacalorie per hour"
        case 1196:
            return "Megajoule per hour"
        case 1197:
            return "British thermal unit per hour"
        case 1198:
            return "Horsepower"
        case 1199:
            return "Watt per meter-Kelvin"
        case 1200:
            return "Watt per square meter-Kelvin"
        case 1201:
            return "Square meter-Kelvin per Watt"
        case 1202:
            return "Joule per Kelvin"
        case 1203:
            return "Kilojoule per Kelvin"
        case 1204:
            return "Joule per kilogram-Kelvin"
        case 1205:
            return "Kilojoule per kilogram-Kelvin"
        case 1206:
            return "Joule per kilogram"
        case 1207:
            return "Megajoule per kilogram"
        case 1208:
            return "Kilojoule per kilogram"
        case 1209:
            return "Ampere"
        case 1210:
            return "Kiloampere"
        case 1211:
            return "Milliampere"
        case 1212:
            return "Microampere"
        case 1213:
            return "Nanoampere"
        case 1214:
            return "Picoampere"
        case 1215:
            return "Coulomb"
        case 1216:
            return "Megacoulomb"
        case 1217:
            return "Kilocoulomb"
        case 1218:
            return "Microcoulomb"
        case 1219:
            return "Nanocoulomb"
        case 1220:
            return "Picocoulomb"
        case 1221:
            return "Ampere-hour"
        case 1222:
            return "Coulomb per cubic meter"
        case 1223:
            return "Coulomb per cubic millimeter"
        case 1224:
            return "Coulomb per cubic centimeter"
        case 1225:
            return "Kilocoulomb per cubic meter"
        case 1226:
            return "Millicoulomb per cubic meter"
        case 1227:
            return "Microcoulomb per cubic meter"
        case 1228:
            return "Coulomb per square meter"
        case 1229:
            return "Coulomb per square millimeter"
        case 1230:
            return "Coulomb per square centimeter"
        case 1231:
            return "Kilocoulomb per square meter"
        case 1232:
            return "Millicoulomb per square meter"
        case 1233:
            return "Microcoulomb per square meter"
        case 1234:
            return "Volt per meter"
        case 1235:
            return "Megavolt per meter"
        case 1236:
            return "Kilovolt per meter"
        case 1237:
            return "Volt per centimeter"
        case 1238:
            return "Millivolt per meter"
        case 1239:
            return "Microvolt per meter"
        case 1240:
            return "Volt"
        case 1241:
            return "Megavolt"
        case 1242:
            return "Kilovolt"
        case 1243:
            return "Millivolt"
        case 1244:
            return "Microvolt"
        case 1245:
            return "Farad"
        case 1246:
            return "Millifarad"
        case 1247:
            return "Microfarad"
        case 1248:
            return "Nanofarad"
        case 1249:
            return "Picofarad"
        case 1250:
            return "Farad per meter"
        case 1251:
            return "Microfarad per meter"
        case 1252:
            return "Nanofarad per meter"
        case 1253:
            return "Picofarad per meter"
        case 1254:
            return "Coulomb-meter"
        case 1255:
            return "Ampere per square meter"
        case 1256:
            return "Megaampere per square meter"
        case 1257:
            return "Ampere per square centimeter"
        case 1258:
            return "Kiloampere per square meter"
        case 1259:
            return "Ampere per meter"
        case 1260:
            return "Kiloampere per meter"
        case 1261:
            return "Ampere per centimeter"
        case 1262:
            return "Tesla"
        case 1263:
            return "Millitesla"
        case 1264:
            return "Microtesla"
        case 1265:
            return "Nanotesla"
        case 1266:
            return "Weber"
        case 1267:
            return "Milliweber"
        case 1268:
            return "Weber per meter"
        case 1270:
            return "Henry"
        case 1271:
            return "Millihenry"
        case 1272:
            return "Microhenry"
        case 1273:
            return "Nanohenry"
        case 1274:
            return "Picohenry"
        case 1275:
            return "Henry per meter"
        case 1276:
            return "Microhenry per meter"
        case 1277:
            return "Nanohenry per meter"
        case 1278:
            return "Ampere-square meter"
        case 1279:
            return "Newton-square meter per Ampere"
        case 1280:
            return "Weber-meter"
        case 1281:
            return "Ohm"
        case 1282:
            return "Gigaohm"
        case 1283:
            return "Megaohm"
        case 1284:
            return "Kiloohm"
        case 1285:
            return "Milliohm"
        case 1286:
            return "Microohm"
        case 1287:
            return "Siemens"
        case 1288:
            return "Kilosiemens"
        case 1289:
            return "Millisiemens"
        case 1290:
            return "Microsiemens"    
        case 1291:
            return "Ohm meter"
        case 1292:
            return "Gigaohm meter"
        case 1293:
            return "Megaohm meter"
        case 1294:
            return "Kiloohm meter"
        case 1295:
            return "Ohm centimeter"
        case 1296:
            return "Milliohm meter"
        case 1297:
            return "Microohm meter"
        case 1298:
            return "Nanoohm meter"
        case 1299:
            return "Siemens per meter"
        case 1300:
            return "Megasiemens per meter"
        case 1301:
            return "Kilosiemens per meter"
        case 1302:
            return "Millisiemens per centimeter"
        case 1303:
            return "Microsiemens per millimeter"
        case 1304:
            return "Per Henry"
        case 1305:
            return "Steradian"
        case 1306:
            return "Watt per steradian"
        case 1307:
            return "Watt per steradian-square meter"
        case 1308:
            return "Watt per square meter"
        case 1309:
            return "Lumen"
        case 1310:
            return "Lumen second"
        case 1311:
            return "Lumen hour"
        case 1312:
            return "Lumen per square meter"
        case 1313:
            return "Lumen per Watt"
        case 1314:
            return "Lux"
        case 1315:
            return "Lux second"
        case 1316:
            return "Candela"
        case 1317:
            return "Candela per square meter"
        case 1318:
            return "Gram per second"
        case 1319:
            return "Gram per minute"
        case 1320:
            return "Gram per hour"
        case 1321:
            return "Gram per day"
        case 1322:
            return "Kilogram per second"
        case 1323:
            return "Kilogram per minute"
        case 1324:
            return "Kilogram per hour"
        case 1325:
            return "Kilogram per day"
        case 1326:
            return "Metric ton per second"
        case 1327:
            return "Metric ton per minute"
        case 1328:
            return "Metric ton per hour"
        case 1329:
            return "Metric ton per day"
        case 1330:
            return "Pound per second"
        case 1331:
            return "Pound per minute"
        case 1332:
            return "Pound per hour"
        case 1333:
            return "Pound per day"
        case 1334:
            return "US ton per second"
        case 1335:
            return "US ton per minute"
        case 1336:
            return "US ton per hour"
        case 1337:
            return "US ton per day"
        case 1338:
            return "Imperial ton per second"
        case 1339:
            return "Imperial ton per minute"
        case 1340:
            return "Imperial ton per hour"
        case 1341:
            return "Imperial ton per day"
        case 1342:
            return "Percent"
        case 1343:
            return "Percent solids by weight"
        case 1344:
            return "Percent solids by volume"
        case 1345:
            return "Percent steam quality"
        case 1346:
            return "Degrees Plato"
        case 1347:
            return "Cubic meter per second"
        case 1348:
            return "Cubic meter per minute"
        case 1349:
            return "Cubic meter per hour"
        case 1350:
            return "Cubic meter per day"
        case 1351:
            return "Liter per second"
        case 1352:
            return "Liter per minute"
        case 1353:
            return "Liter per hour"
        case 1354:
            return "Liter per day"
        case 1355:
            return "Megaliter per day"
        case 1356:
            return "Cubic foot per second"
        case 1357:
            return "Cubic foot per minute"
        case 1358:
            return "Cubic foot per hour"
        case 1359:
            return "Cubic foot per day"
        case 1360:
            return "Standard cubic foot per minute"
        case 1361:
            return "Standard cubic foot per hour"
        case 1362:
            return "US gallon per second"
        case 1363:
            return "US gallon per minute"
        case 1364:
            return "US gallon per hour"
        case 1365:
            return "US gallon per day"
        case 1366:
            return "Mega US gallon per day"
        case 1367:
            return "Imperial gallon per second"
        case 1368:
            return "Imperial gallon per minute"
        case 1369:
            return "Imperial gallon per hour"
        case 1370:
            return "Imperial gallon per day"
        case 1371:
            return "Barrel per second"
        case 1372:
            return "Barrel per minute"
        case 1373:
            return "Barrel per hour"
        case 1374:
            return "Barrel per day"
        case 1375:
            return "Watt per square meter"
        case 1376:
            return "Milliwatt per square meter"
        case 1377:
            return "Microwatt per square meter"
        case 1378:
            return "Picowatt per square meter"
        case 1379:
            return "Pascal second per cubic meter"
        case 1380:
            return "Newton second per meter"
        case 1381:
            return "Pascal second per meter"
        case 1382:
            return "Bel"
        case 1383:
            return "Decibel"
        case 1384:
            return "Mole"
        case 1385:
            return "Kilomole"
        case 1386:
            return "Millimole"
        case 1387:
            return "Micromole"
        case 1388:
            return "Kilogram per mole"
        case 1389:
            return "Gram per mole"
        case 1390:
            return "Cubic meter per mole"
        case 1391:
            return "Cubic decimeter per mole"
        case 1392:
            return "Cubic centimeter per mole"
        case 1393:
            return "Liter per mole"
        case 1394:
            return "Joule per mole"
        case 1395:
            return "Kilojoule per mole"
        case 1396:
            return "Joule per mole-Kelvin"
        case 1397:
            return "Mole per cubic meter"
        case 1398:
            return "Mole per cubic decimeter"
        case 1399:
            return "Mole per liter"
        case 1400:
            return "Mole per kilogram"
        case 1401:
            return "Millimole per kilogram"
        case 1402:
            return "Becquerel"
        case 1403:
            return "Megabecquerel"
        case 1404:
            return "Kilobecquerel"
        case 1405:
            return "Becquerel per kilogram"
        case 1406:
            return "Kilobecquerel per kilogram"
        case 1407:
            return "Megabecquerel per kilogram"
        case 1408:
            return "Gray"
        case 1409:
            return "Milligray"
        case 1410:
            return "Rad"
        case 1411:
            return "Sievert"
        case 1412:
            return "Millisievert"
        case 1413:
            return "Rem"
        case 1414:
            return "Coulomb per kilogram"
        case 1415:
            return "Millicoulomb per kilogram"
        case 1416:
            return "Roentgen"
        case 1417:
            return "Magnetic energy density"
        case 1418:
            return ""
        case 1419:
            return "Cubic meter per coulomb"
        case 1420:
            return "Volt per Kelvin"
        case 1421:
            return "Millivolt per Kelvin"
        case 1422:
            return "pH value"
        case 1423:
            return "Parts per million"
        case 1424:
            return "Parts per billion"
        case 1425:
            return "Parts per trillion"
        case 1426:
            return "Degrees Brix"
        case 1427:
            return "Degrees Balling"
        case 1428:
            return "Proof by volume"
        case 1429:
            return "Proof by mass"
        case 1430:
            return "Pound per Imperial gallon"
        case 1431:
            return "Kilocalorie per second"
        case 1432:
            return "Kilocalorie per minute"
        case 1433:
            return "Kilocalorie per hour"
        case 1434:
            return "Kilocalorie per day"
        case 1435:
            return "Megacalorie per second"
        case 1436:
            return "Megacalorie per minute"
        case 1437:
            return "Megacalorie per day"
        case 1438:
            return "Kilojoule per second"
        case 1439:
            return "Kilojoule per minute"
        case 1440:
            return "Kilojoule per hour"
        case 1441:
            return "Kilojoule per day"
        case 1442:
            return "Megajoule per second"
        case 1443:
            return "Megajoule per minute"
        case 1444:
            return "Megajoule per day"
        case 1445:
            return "British thermal unit per second"
        case 1446:
            return "British thermal unit per minute"
        case 1447:
            return "British thermal unit per day"
        case 1448:
            return "Micro US gallon per second"
        case 1449:
            return "Milli US gallon per second"
        case 1450:
            return "Kilo US gallon per second"
        case 1451:
            return "Mega US gallon per second"
        case 1452:
            return "Micro US gallon per minute"
        case 1453:
            return "Milli US gallon per minute"
        case 1454:
            return "Kilo US gallon per minute"
        case 1455:
            return "Mega US gallon per minute"
        case 1456:
            return "Micro US gallon per hour"
        case 1457:
            return "Milli US gallon per hour"
        case 1458:
            return "Kilo US gallon per hour"
        case 1459:
            return "Mega US gallon per hour"
        case 1460:
            return "Micro US gallon per day"
        case 1461:
            return "Milli US gallon per day"
        case 1462:
            return "Kilo US gallon per day"
        case 1463:
            return "Micro Imperial gallon per second"
        case 1464:
            return "Milli Imperial gallon per second"
        case 1465:
            return "Kilo Imperial gallon per second"
        case 1466:
            return "Mega Imperial gallon per second"
        case 1467:
            return "Micro Imperial gallon per minute"
        case 1468:
            return "Milli Imperial gallon per minute"
        case 1469:
            return "Kilo Imperial gallon per minute"
        case 1470:
            return "Mega Imperial gallon per minute"
        case 1471:
            return "Micro Imperial gallon per hour"
        case 1472:
            return "Milli Imperial gallon per hour"
        case 1473:
            return "Kilo Imperial gallon per hour"
        case 1474:
            return "Mega Imperial gallon per hour"
        case 1475:
            return "Micro Imperial gallon per day"
        case 1476:
            return "Milli Imperial gallon per day"
        case 1477:
            return "Kilo Imperial gallon per day"
        case 1478:
            return "Mega Imperial gallon per day"
        case 1479:
            return "Micro barrel per second"
        case 1480:
            return "Milli barrel per second"
        case 1481:
            return "Kilo barrel per second"
        case 1482:
            return "Mega barrel per second"
        case 1483:
            return "Micro barrel per minute"
        case 1484:
            return "Milli barrel per minute"
        case 1485:
            return "Kilo barrel per minute"
        case 1486:
            return "Mega barrel per minute"
        case 1487:
            return "Micro barrel per hour"
        case 1488:
            return "Milli barrel per hour"
        case 1489:
            return "Kilo barrel per hour"
        case 1490:
            return "Mega barrel per hour"
        case 1491:
            return "Micro barrel per day"
        case 1492:
            return "Milli barrel per day"
        case 1493:
            return "Kilo barrel per day"
        case 1494:
            return "Mega barrel per day"
        case 1495:
            return "Cubic micrometer per second"
        case 1496:
            return "Cubic millimeter per second"
        case 1497:
            return "Cubic kilometer per second"
        case 1498:
            return "Cubic megameter per second"
        case 1499:
            return "Cubic micrometer per minute"
        case 1500:
            return "Cubic millimeter per minute"
        case 1501:
            return "Cubic kilometer per minute"
        case 1502:
            return "Cubic megameter per minute"
        case 1503:
            return "Cubic micrometer per hour"
        case 1504:
            return "Cubic millimeter per hour"
        case 1505:
            return "Cubic kilometer per hour"
        case 1506:
            return "Cubic megameter per hour"
        case 1507:
            return "Cubic micrometer per day"
        case 1508:
            return "Cubic millimeter per day"
        case 1509:
            return "Cubic kilometer per day"
        case 1510:
            return "Cubic megameter per day"
        case 1511:
            return "Cubic centimeter per second"
        case 1512:
            return "Cubic centimeter per minute"
        case 1513:
            return "Cubic centimeter per hour"
        case 1514:
            return "Cubic centimeter per day"
        case 1515:
            return "Kilocalorie per kilogram"
        case 1516:
            return "British thermal unit per pound"
        case 1517:
            return "Kiloliter"
        case 1518:
            return "Kiloliter per minute"
        case 1519:
            return "Kiloliter per hour"
        case 1520:
            return "Kiloliter per day"
        case 1551:
            return "Siemens per centimeter"
        case 1552:
            return "Microsiemens per centimeter"
        case 1553:
            return "Millisiemens per meter"
        case 1554:
            return "Microsiemens per meter"
        case 1555:
            return "Megaohm centimeter"
        case 1556:
            return "Kiloohm centimeter"
        case 1557:
            return "Weight percent"
        case 1558:
            return "Milligram per liter"
        case 1559:
            return "Microgram per liter"
        case 1560:
            return "-"
        case 1561:
            return "-"
        case 1562:
            return "Volume percent"
        case 1563:
            return "Milliliter per minute"
        case 1564:
            return "Milligram per cubic centimeter"
        case 1565:
            return "Milligram per liter"
        case 1566:
            return "Milligram per cubic meter"
        case 1567:
            return "Carat"
        case 1568:
            return "Pound (troy or apothecary)"
        case 1569:
            return "Ounce (troy or apothecary)"
        case 1570:
            return "Ounce (U.S. fluid)"
        case 1571:
            return "Cubic centimeter"
        case 1572:
            return "Acre foot"
        case 1573:
            return "Cubic meter"
        case 1574:
            return "Liter"
        case 1575:
            return "Standard cubic meter"
        case 1576:
            return "Standard liter"
        case 1577:
            return "Milliliter per second"
        case 1578:
            return "Milliliter per hour"
        case 1579:
            return "Milliliter per day"
        case 1580:
            return "Acre foot per second"
        case 1581:
            return "Acre foot per minute"
        case 1582:
            return "Acre foot per hour"
        case 1583:
            return "Acre foot per day"
        case 1584:
            return "Ounce per second"
        case 1585:
            return "Ounce per minute"
        case 1586:
            return "Ounce per hour"
        case 1587:
            return "Ounce per day"
        case 1588:
            return "Standard cubic meter per second"
        case 1589:
            return "Standard cubic meter per minute"
        case 1590:
            return "Standard cubic meter per hour"
        case 1591:
            return "Standard cubic meter per day"
        case 1592:
            return "Standard liter per second"
        case 1593:
            return "Standard liter per minute"
        case 1594:
            return "Standard liter per hour"
        case 1595:
            return "Standard liter per day"
        case 1596:
            return "Standard cubic meter per second"
        case 1597:
            return "Standard cubic meter per minute"
        case 1598:
            return "Standard cubic meter per hour"
        case 1599:
            return "Standard cubic meter per day"
        case 1600:
            return "Standard liter per second"
        case 1601:
            return "Standard liter per minute"
        case 1602:
            return "Standard liter per hour"
        case 1603:
            return "Standard liter per day"
        case 1604:
            return "Standard cubic foot per second"
        case 1605:
            return "Standard cubic foot per day"
        case 1606:
            return "Ounce per second"
        case 1607:
            return "Ounce per minute"
        case 1608:
            return "Ounce per hour"
        case 1609:
            return "Ounce per day"
        case 1610:
            return "Pascal (absolute)"
        case 1611:
            return "Pascal (gauge)"
        case 1612:
            return "Gigapascal (absolute)"
        case 1613:
            return "Gigapascal (gauge)"
        case 1614:
            return "Megapascal (absolute)"
        case 1615:
            return "Megapascal (gauge)"
        case 1616:
            return "Kilopascal (absolute)"
        case 1617:
            return "Kilopascal (gauge)"
        case 1618:
            return "Millipascal (absolute)"
        case 1619:
            return "Millipascal (gauge)"
        case 1620:
            return "Micropascal (absolute)"
        case 1621:
            return "Micropascal (gauge)"
        case 1622:
            return "Hectopascal (absolute)"
        case 1623:
            return "Hectopascal (gauge)"
        case 1624:
            return ""
        case 1625:
            return ""
        case 1626:
            return ""
        case 1627:
            return ""
        case 1628:
            return "Standard density at 4°C"
        case 1629:
            return "Standard density at 15°C"
        case 1630:
            return "Standard density at 20°C"
        case 1631:
            return "Metric horsepower"
        case 1632:
            return "Parts per trillion"
        case 1633:
            return "Hectoliter per second"
        case 1634:
            return "Hectoliter per minute"
        case 1635:
            return "Hectoliter per hour"
        case 1636:
            return "Hectoliter per day"
        case 1637:
            return "Barrel (US fluid) per second"
        case 1638:
            return "Barrel (US fluid) per minute"
        case 1639:
            return "Barrel (US fluid) per hour"
        case 1640:
            return "Barrel (US fluid) per day"
        case 1641:
            return "Barrel (U.S. federal)"
        case 1642:
            return "Barrel (U.S. federal) per second"
        case 1643:
            return "Barrel (U.S. federal) per minute"
        case 1644:
            return "Barrel (U.S. federal) per hour"
        case 1645:
            return "Barrel (U.S. federal) per day"
        case 1998:
            return "Unit not known"
        case 1999:
            return "Special"



### start main
def getMtps(input_files=None, logger=None) -> list[Pea]:
    mtps:list[Pea] = []

    if input_files is None:
        input_files =  TESTMTPS     # 如果没传参数，可以保留原来的测试数据作为默认值

    # parse mtp files
    for file in input_files:
        tree = parse(file)
        root = tree.getroot()

        # create mtp object
        mtp = Pea()
        mtps.append(mtp)

        # parse mtp
        for child in root:
            if child.tag == f"{NAMESPACE}InstanceHierarchy" and child.get("Name") == "ModuleTypePackage":
                # fetch name of mtp
                mtp.nameMtp(name=child.find(f"{NAMESPACE}InternalElement").get("Name"))

                for gchild in child.iter(f"{NAMESPACE}InternalElement"):
                    if gchild.get("Name") == "CommunicationSet" or gchild.get("Name") == "Communication":
                        for node in gchild:
                            if node.get("Name") == "InstanceList" or node.get("Name") == "Instances":
                                # parse instances
                                for instNode in node.iter(f"{NAMESPACE}InternalElement"):
                                    if (instNode.get("Name") == "InstanceList" or 
                                        instNode.get("Name") == "Instances" or
                                        instNode.get("RefBaseSystemUnitPath") == "MTPDataObjectSUCLib/DataAssembly/PeaElement/PeaInformationLabel" or
                                        instNode.get("RefBaseSystemUnitPath") == "MTPDataObjectSUCLib/DataAssembly/PeaElement/WebServerUrlInfo" or
                                        instNode.get("RefBaseSystemUnitPath") == "MTPDataObjectSUCLib/DataAssembly/ServiceElement/ProcedureHealthView"
                                        ):    #or instNode.get("RefBaseSystemUnitPath") == "MTPDataObjectSUCLib/DataAssembly/ServiceElement/ProcedureHealthView" 排除了procedures, 因为procedures在service里有另外的节点
                                        continue
                                    inst = Instance(name=instNode.get("Name"), id=instNode.get("ID"))

                                    for attrNode in instNode.iter(f"{NAMESPACE}Attribute"):
                                        if attrNode.get("Name") == "RefID":
                                            inst.addRefId(attrNode.findtext(f"{NAMESPACE}Value"))
                                        elif attrNode.get("Name") == "WQC":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['WQC']['ID'] = id
                                            inst.paramElem['WQC']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "OSLevel":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['OSLevel']['ID'] = id
                                            inst.paramElem['OSLevel']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "CommandInfo":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['CommandInfo']['ID'] = id
                                            inst.paramElem['CommandInfo']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "CommandOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['CommandOp']['ID'] = id
                                            inst.paramElem['CommandOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "CommandInt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['CommandInt']['ID'] = id
                                            inst.paramElem['CommandInt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "CommandExt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['CommandExt']['ID'] = id
                                            inst.paramElem['CommandExt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ProcedureOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ProcedureOp']['ID'] = id
                                            inst.paramElem['ProcedureOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ProcedureInt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ProcedureInt']['ID'] = id
                                            inst.paramElem['ProcedureInt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ProcedureExt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ProcedureExt']['ID'] = id
                                            inst.paramElem['ProcedureExt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateCur":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateCur']['ID'] = id
                                            inst.paramElem['StateCur']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "CommandEn":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['CommandEn']['ID'] = id
                                            inst.paramElem['CommandEn']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ProcedureCur":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ProcedureCur']['ID'] = id
                                            inst.paramElem['ProcedureCur']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ProcedureReq":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ProcedureReq']['ID'] = id
                                            inst.paramElem['ProcedureReq']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "PosTextID":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['PosTextID']['ID'] = id
                                            inst.paramElem['PosTextID']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "InteractQuestionID":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['InteractQuestionID']['ID'] = id
                                            inst.paramElem['InteractQuestionID']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "InteractAnswerID":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['InteractAnswerID']['ID'] = id
                                            inst.paramElem['InteractAnswerID']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "InteractAddInfo":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['InteractAddInfo']['ID'] = id
                                            inst.paramElem['InteractAddInfo']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateChannel":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateChannel']['ID'] = id
                                            inst.paramElem['StateChannel']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateOffAut":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateOffAut']['ID'] = id
                                            inst.paramElem['StateOffAut']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateOpAut":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateOpAut']['ID'] = id
                                            inst.paramElem['StateOpAut']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateAutAut":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateAutAut']['ID'] = id
                                            inst.paramElem['StateAutAut']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateOffOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateOffOp']['ID'] = id
                                            inst.paramElem['StateOffOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateOpOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateOpOp']['ID'] = id
                                            inst.paramElem['StateOpOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateAutOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateAutOp']['ID'] = id
                                            inst.paramElem['StateAutOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateOpAct":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateOpAct']['ID'] = id
                                            inst.paramElem['StateOpAct']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateAutAct":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateAutAct']['ID'] = id
                                            inst.paramElem['StateAutAct']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "StateOffAct":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['StateOffAct']['ID'] = id
                                            inst.paramElem['StateOffAct']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "SrcChannel":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['SrcChannel']['ID'] = id
                                            inst.paramElem['SrcChannel']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "SrcExtAut":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['SrcExtAut']['ID'] = id
                                            inst.paramElem['SrcExtAut']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "SrcIntAut":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['SrcIntAut']['ID'] = id
                                            inst.paramElem['SrcIntAut']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "SrcExtOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['SrcExtOp']['ID'] = id
                                            inst.paramElem['SrcExtOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "SrcIntOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['SrcIntOp']['ID'] = id
                                            inst.paramElem['SrcIntOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "SrcIntAct":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['SrcIntAct']['ID'] = id
                                            inst.paramElem['SrcIntAct']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "SrcExtAct":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['SrcExtAct']['ID'] = id
                                            inst.paramElem['SrcExtAct']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ProcParamApplyEn":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ProcParamApplyEn']['ID'] = id
                                            inst.paramElem['ProcParamApplyEn']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ProcParamApplyExt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ProcParamApplyExt']['ID'] = id
                                            inst.paramElem['ProcParamApplyExt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ProcParamApplyOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ProcParamApplyOp']['ID'] = id
                                            inst.paramElem['ProcParamApplyOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ProcParamApplyInt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ProcParamApplyInt']['ID'] = id
                                            inst.paramElem['ProcParamApplyInt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ConfigParamApplyEn":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ConfigParamApplyEn']['ID'] = id
                                            inst.paramElem['ConfigParamApplyEn']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ConfigParamApplyExt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ConfigParamApplyExt']['ID'] = id
                                            inst.paramElem['ConfigParamApplyExt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ConfigParamApplyOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ConfigParamApplyOp']['ID'] = id
                                            inst.paramElem['ConfigParamApplyOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ConfigParamApplyInt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ConfigParamApplyInt']['ID'] = id
                                            inst.paramElem['ConfigParamApplyInt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ReportValueFreeze":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ReportValueFreeze']['ID'] = id
                                            inst.paramElem['ReportValueFreeze']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ApplyEn":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ApplyEn']['ID'] = id
                                            inst.paramElem['ApplyEn']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ApplyExt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ApplyExt']['ID'] = id
                                            inst.paramElem['ApplyExt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ApplyOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ApplyOp']['ID'] = id
                                            inst.paramElem['ApplyOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "ApplyInt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['ApplyInt']['ID'] = id
                                            inst.paramElem['ApplyInt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "Sync":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['Sync']['ID'] = id
                                            inst.paramElem['Sync']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "VExt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VExt']['ID'] = id
                                            inst.paramElem['VExt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "VInt":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VInt']['ID'] = id
                                            inst.paramElem['VInt']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "VOp":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VOp']['ID'] = id
                                            inst.paramElem['VOp']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "VReq":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VReq']['ID'] = id
                                            inst.paramElem['VReq']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                            inst.default = float(attrNode.findtext(f"{NAMESPACE}DefaultValue"))
                                        elif attrNode.get("Name") == "VFbk":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VFbk']['ID'] = id
                                            inst.paramElem['VFbk']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "VOut":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VOut']['ID'] = id
                                            inst.paramElem['VOut']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "V":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['V']['ID'] = id
                                            inst.paramElem['V']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "Pos":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['Pos']['ID'] = id
                                            inst.paramElem['Pos']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "Ctrl":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['Ctrl']['ID'] = id
                                            inst.paramElem['Ctrl']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "FwdCtrl":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['FwdCtrl']['ID'] = id
                                            inst.paramElem['FwdCtrl']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "RevCtrl":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['RevCtrl']['ID'] = id
                                            inst.paramElem['RevCtrl']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "VSclMin":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VSclMin']['ID'] = id
                                            inst.paramElem['VSclMin']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "VSclMax":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VSclMax']['ID'] = id
                                            inst.paramElem['VSclMax']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                        elif attrNode.get("Name") == "VMin":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VMin']['ID'] = id
                                            inst.paramElem['VMin']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                            inst.addMin(float(attrNode.findtext(f"{NAMESPACE}DefaultValue")))
                                        elif attrNode.get("Name") == "VMax":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VMax']['ID'] = id
                                            inst.paramElem['VMax']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                            inst.addMax(float(attrNode.findtext(f"{NAMESPACE}DefaultValue")))
                                        elif attrNode.get("Name") == "VUnit":
                                            elemNode = attrNode.findtext(f"{NAMESPACE}Value")
                                            id = gchild.findtext(f".//{NAMESPACE}ExternalInterface[@ID='{elemNode}']/{NAMESPACE}Attribute[@Name='Identifier']/{NAMESPACE}Value")
                                            inst.paramElem['VUnit']['ID'] = id
                                            inst.paramElem['VUnit']['Default'] = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                            unitId = attrNode.findtext(f"{NAMESPACE}DefaultValue")
                                            inst.unitval = int(unitId)
                                            inst.addUnit(getUnit(int(unitId)))

                                    # add instance to mtp
                                    mtp.addInstance(inst)
                            elif node.get("Name") == "SourceList" or node.get("Name") == "Sources":
                                # parse url
                                mtp.addUrl(url=node.findtext(f".//*[@Name='Endpoint']/{NAMESPACE}Value"))
                                # parse namespace
                                mtp.ns = node.findtext(f".//*[@Name='Namespace']/{NAMESPACE}Value")

            elif child.tag == f"{NAMESPACE}InstanceHierarchy" and child.get("Name") == "Services":
                for gchild in child:
                    if gchild.tag == f"{NAMESPACE}InternalElement":
                        keys = ['CommandEn',
                                'CommandExt',
                                'CommandInt',
                                'CommandOp',
                                'ConfigParamApplyEn',
                                'ConfigParamApplyExt',
                                'ConfigParamApplyInt',
                                'ConfigParamApplyOp',
                                'InteractAddInfo',
                                'InteractAnswerID',
                                'InteractQuestionID',
                                'OSLevel',
                                'PosTextID',
                                'ProcParamApplyEn',
                                'ProcParamApplyExt',
                                'ProcParamApplyInt',
                                'ProcParamApplyOp',
                                'ProcedureCur',
                                'ProcedureExt',
                                'ProcedureInt',
                                'ProcedureOp',
                                'ProcedureReq',
                                'ReportValueFreeze',
                                'SrcChannel',
                                'SrcExtAct',
                                'SrcExtAut',
                                'SrcExtOp',
                                'SrcIntAct',
                                'SrcIntAut',
                                'SrcIntOp',
                                'StateAutAct',
                                'StateAutAut',
                                'StateAutOp',
                                'StateChannel',
                                'StateCur',
                                'StateOffAct',
                                'StateOffAut',
                                'StateOffOp',
                                'StateOpAct',
                                'StateOpAut',
                                'StateOpOp']

                        inst = mtp.getInstance(instId=gchild.findtext(f"./{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value"))
                        serv = Service()
                        serv.name = gchild.get("Name") # name of the service
                        serv.id = gchild.get("ID") # id of the service
                        serv.refid = gchild.findtext(f"./{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value")
                        for key in keys:
                            serv.paramElem[key] = inst.paramElem[key]
                        mtp.addService(serv)

                        # get procedures
                        for ggchild in gchild:
                            if ggchild.tag == f"{NAMESPACE}InternalElement":
                                procName = ggchild.get("Name") # name of the procedure
                                procId = ggchild.findtext(f"./{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value") # id of the procedure
                                proc = Procedure(name=procName, id=procId)
                                serv.procs.append(proc)
                                mtp.procs.append(proc)
                                proc.serviceId = serv.id

                                for paramNode in ggchild:
                                    # if paramNode.tag == f"{NAMESPACE}InternalElement":
                                    if paramNode.tag == f"{NAMESPACE}InternalElement" and paramNode.get("RefBaseSystemUnitPath") != "MTPServiceSUCLib/RequiredEquipment":     # MODIFIED: 把RefBaseSystemUnitPath="MTPServiceSUCLib/RequiredEquipment （sensor/actuator）去掉
                                        for refNode in paramNode.iter(f"{NAMESPACE}Attribute"):
                                            if refNode.get("Name") == "RefID" and mtp.hasInstance(refNode.findtext(f"{NAMESPACE}Value")):
                                                # get the instance the procedure refers to
                                                procParam = mtp.getInstance(refNode.findtext(f"{NAMESPACE}Value"))

                                                # add the instance to the procedure's params
                                                proc.addParameter(procParam)
                                    elif paramNode.tag == f"{NAMESPACE}Attribute" and paramNode.get("Name") == "IsSelfCompleting":
                                        proc.setSelfCompleting(paramNode.findtext(f"{NAMESPACE}Value"))
                                    elif paramNode.tag == f"{NAMESPACE}Attribute" and paramNode.get("Name") == "ProcedureID":
                                        proc.procId = int(paramNode.findtext(f"{NAMESPACE}Value"))

            elif child.tag == f"{NAMESPACE}InstanceHierarchy" and child.get("Name") == "HMI":
                # parse HMI Information for HC10/HC2040
                children = child.findall(".//*[@RefBaseSystemUnitPath='MTPHMISUCLib/Picture']")
                if len(children) == 1:
                    # HC2040
                    # create HMI instance
                    hmi = HMI()
                    # set type to RI because HC2040 doesn't support services
                    hmi.type = "RI"
                    # set width, height and hierarchy level
                    for gchild in children[0]:
                        if gchild.tag == f"{NAMESPACE}Attribute":
                            # width
                            if gchild.get("Name") == "Width":
                                if int(gchild.findtext(f"{NAMESPACE}Value")) is not None:
                                    hmi.width = int(gchild.findtext(f"{NAMESPACE}Value"))
                                elif int(gchild.findtext(f"{NAMESPACE}DefaultValue")) is not None:
                                    hmi.width = int(gchild.findtext(f"{NAMESPACE}DefaultValue"))
                            # height
                            elif gchild.get("Name") == "Height":
                                if int(gchild.findtext(f"{NAMESPACE}Value")) is not None:
                                    hmi.height = int(gchild.findtext(f"{NAMESPACE}Value"))
                                elif int(gchild.findtext(f"{NAMESPACE}DefaultValue")) is not None:
                                    hmi.height = int(gchild.findtext(f"{NAMESPACE}DefaultValue"))
                            # hierarchy level
                            elif gchild.get("Name") == "HierarchyLevel":
                                if gchild.findtext(f"{NAMESPACE}Value") is not None:
                                    hmi.hierarchy = gchild.findtext(f"{NAMESPACE}Value")
                                elif gchild.findtext(f"{NAMESPACE}DefaultValue") is not None:
                                    hmi.hierarchy = gchild.findtext(f"{NAMESPACE}DefaultValue")
                        elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/VisualObject":
                            # add visual objects
                            visObj = VisualObject()
                            visObj.name = gchild.get("Name")
                            # width
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}Value") is not None:
                                visObj.width = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}DefaultValue") is not None:
                                visObj.width = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}DefaultValue")
                            # height
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}Value") is not None:
                                visObj.height = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}DefaultValue") is not None:
                                visObj.height = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}DefaultValue")
                            # x coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                visObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                visObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                visObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                visObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                            # z index
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value") is not None:
                                visObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue") is not None:
                                visObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue")
                            # rotation
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}Value") is not None:
                                visObj.rotation = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}DefaultValue") is not None:
                                visObj.rotation = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}DefaultValue")
                            # eClass Version
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}Value") is not None:
                                visObj.eClassVer = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}DefaultValue") is not None:
                                visObj.eClassVer = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}DefaultValue")
                            # eClass Classification Class
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}Value") is not None:
                                visObj.eClassClass = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}DefaultValue") is not None:
                                visObj.eClassClass = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}DefaultValue")
                            # eClass IRDI
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}Value") is not None:
                                visObj.eClassIRDI = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}DefaultValue") is not None:
                                visObj.eClassIRDI = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}DefaultValue")
                            # refId
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value") is not None:
                                visObj.refId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}DefaultValue") is not None:
                                visObj.refId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}DefaultValue")
                            # refInstance
                            visObj.refInst = mtp.getInstance(instId=visObj.refId)

                            # find nodes that have port information
                            portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                            for pn in portNodes:
                                # create port
                                port = Port()
                                port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                port.name = pn.get("Name")
                                # x coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                # y coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")

                                visObj.ports.append(port)
                            hmi.visuals.append(visObj)
                        elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/TopologyObject/Junction":
                            # add junction objects
                            junc = Junction()
                            junc.name = gchild.get("Name")
                            # x coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                junc.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                junc.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                junc.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                junc.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")

                            # find nodes that have port information
                            portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                            for pn in portNodes:
                                # create port
                                port = Port()
                                port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                port.name = pn.get("Name")
                                # x coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                # y coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                
                                junc.ports.append(port)
                            hmi.juncts.append(junc)
                        elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/TopologyObject/Termination/Sink":
                            # add sink objects
                            sinkObj = Sink()
                            sinkObj.name = gchild.get("Name")
                            # x coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                sinkObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                sinkObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                sinkObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                sinkObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                            # term ID
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value") is not None:
                                sinkObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue") is not None:
                                sinkObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue")
                            
                            # find nodes that have port information
                            portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                            for pn in portNodes:
                                # create port
                                port = Port()
                                port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                port.name = pn.get("Name")
                                # x coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                # y coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                
                                sinkObj.ports.append(port)
                            hmi.sinks.append(sinkObj)
                        elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/TopologyObject/Termination/Source":
                            # add source objects
                            sourceObj = Source()
                            sourceObj.name = gchild.get("Name")
                            # x coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                sourceObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                sourceObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                sourceObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                sourceObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                            # term ID
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value") is not None:
                                sourceObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue") is not None:
                                sourceObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue")
                            
                            # find nodes that have port information
                            portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                            for pn in portNodes:
                                # create port
                                port = Port()
                                port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                port.name = pn.get("Name")
                                # x coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                # y coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                
                                sourceObj.ports.append(port)
                            hmi.srcs.append(sourceObj)
                        elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/Connection/Pipe":
                            # add pipe objects
                            pipeObj = Pipe()
                            pipeObj.name = gchild.get("Name")
                            # directed flag
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}Value") is not None:
                                pipeObj.direct = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}DefaultValue") is not None:
                                pipeObj.direct = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}DefaultValue")
                            # edge path
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value") is not None:
                                pipeObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue") is not None:
                                pipeObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue")
                            
                            # find nodes that have port information
                            portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                            for pn in portNodes:
                                # create port
                                port = Port()
                                port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                port.name = pn.get("Name")
                                # x coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                # y coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                
                                pipeObj.ports.append(port)
                            hmi.pipes.append(pipeObj)
                        elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/Connection/FunctionLine":
                            # add function line objects
                            functlinObj = Line()
                            functlinObj.type = "Function Line"
                            functlinObj.name = gchild.get("Name")
                            # edge path
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value") is not None:
                                functlinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue") is not None:
                                functlinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue")
                            
                            # find nodes that have port information
                            portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/LogicalPort']")
                            for pn in portNodes:
                                # create port
                                port = Port()
                                port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                port.name = pn.get("Name")
                                # x coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                # y coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                
                                functlinObj.ports.append(port)
                            hmi.lines.append(functlinObj)
                        elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/Connection/MeasurementLine":
                            # add measurement line objects
                            measLinObj = Line()
                            measLinObj.type = "Measurement Line"
                            measLinObj.name = gchild.get("Name")
                            # edge path
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value") is not None:
                                measLinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue") is not None:
                                measLinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue")
                            
                            # find nodes that have port information
                            portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/MeasurementPoint']")
                            for pn in portNodes:
                                # create port
                                port = Port()
                                port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                port.name = pn.get("Name")
                                # x coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                # y coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                
                                measLinObj.ports.append(port)
                            hmi.lines.append(measLinObj)
                        elif gchild.tag == f"{NAMESPACE}InternalLink":
                            # side A
                            sideA = gchild.get("RefPartnerSideA")
                            # side B
                            sideB = gchild.get("RefPartnerSideB")
                            hmi.links.append((sideA, sideB))

                    mtp.hmis.append(hmi)
                else:
                    # HC10
                    for hminode in children:
                        # create hmi instance
                        hmi = HMI()
                        if hminode.get("Name") == "Services":
                            # set type to service
                            hmi.type = "Service"
                            for gchild in hminode:
                                if gchild.tag == f"{NAMESPACE}Attribute":
                                    if gchild.get("Name") == "Width":
                                        if int(gchild.findtext(f"{NAMESPACE}Value")) is not None:
                                            hmi.width = int(gchild.findtext(f"{NAMESPACE}Value"))
                                        elif int(gchild.findtext(f"{NAMESPACE}DefaultValue")) is not None:
                                            hmi.width = int(gchild.findtext(f"{NAMESPACE}DefaultValue"))
                                    elif gchild.get("Name") == "Height":
                                        if int(gchild.findtext(f"{NAMESPACE}Value")) is not None:
                                            hmi.height = int(gchild.findtext(f"{NAMESPACE}Value"))
                                        elif int(gchild.findtext(f"{NAMESPACE}DefaultValue")) is not None:
                                            hmi.height = int(gchild.findtext(f"{NAMESPACE}DefaultValue"))
                                    elif gchild.get("Name") == "HierarchyLevel":
                                        if gchild.findtext(f"{NAMESPACE}Value") is not None:
                                            hmi.hierarchy = gchild.findtext(f"{NAMESPACE}Value")
                                        elif gchild.findtext(f"{NAMESPACE}DefaultValue") is not None:
                                            hmi.hierarchy = gchild.findtext(f"{NAMESPACE}DefaultValue")
                                elif gchild.tag == f"{NAMESPACE}InternalElement":
                                    # add visual object
                                    visObj = VisualObject()
                                    visObj.name = gchild.get("Name")
                                    visObj.refId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value")
                                    visObj.refInst = mtp.getInstance(visObj.refId)
                                    visObj.width = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}Value")
                                    visObj.height = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}Value")
                                    visObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                    visObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                    visObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value")
                                    visObj.rotation = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}Value")
                                    visObj.eClassVer = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}Value")
                                    visObj.eClassClass = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}Value")
                                    visObj.eClassIRDI = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}Value")
                                    hmi.visuals.append(visObj)

                            mtp.hmis.append(hmi)
                        elif hminode.get("Name") == "RI_Fliessbild":
                            # set type to ri
                            hmi.type = "RI"
                            for gchild in hminode:
                                if gchild.tag == f"{NAMESPACE}Attribute":
                                    if gchild.get("Name") == "Width":
                                        if int(gchild.findtext(f"{NAMESPACE}Value")) is not None:
                                            hmi.width = int(gchild.findtext(f"{NAMESPACE}Value"))
                                        elif int(gchild.findtext(f"{NAMESPACE}DefaultValue")) is not None:
                                            hmi.width = int(gchild.findtext(f"{NAMESPACE}DefaultValue"))
                                    elif gchild.get("Name") == "Height":
                                        if int(gchild.findtext(f"{NAMESPACE}Value")) is not None:
                                            hmi.height = int(gchild.findtext(f"{NAMESPACE}Value"))
                                        elif int(gchild.findtext(f"{NAMESPACE}DefaultValue")) is not None:
                                            hmi.height = int(gchild.findtext(f"{NAMESPACE}DefaultValue"))
                                    elif gchild.get("Name") == "HierarchyLevel":
                                        if gchild.findtext(f"{NAMESPACE}Value") is not None:
                                            hmi.hierarchy = gchild.findtext(f"{NAMESPACE}Value")
                                        elif gchild.findtext(f"{NAMESPACE}DefaultValue") is not None:
                                            hmi.hierarchy = gchild.findtext(f"{NAMESPACE}DefaultValue")
                                elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/TopologyObject/Termination/Sink":
                                    # add sink objects
                                    sinkObj = Sink()
                                    sinkObj.name = gchild.get("Name")
                                    # x coordinate
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                        sinkObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                        sinkObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                    # y coordinate
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                        sinkObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                        sinkObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                    # term ID
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value") is not None:
                                        sinkObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue") is not None:
                                        sinkObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue")
                                    
                                    # find nodes that have port information
                                    portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                                    for pn in portNodes:
                                        # create port
                                        port = Port()
                                        port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                        port.name = pn.get("Name")
                                        # x coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                        # y coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                        
                                        sinkObj.ports.append(port)
                                    hmi.sinks.append(sinkObj)
                                elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/TopologyObject/Junction":
                                    # add junction objects
                                    junc = Junction()
                                    junc.name = gchild.get("Name")
                                    # x coordinate
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                        junc.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                        junc.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                    # y coordinate
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                        junc.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                        junc.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")

                                    # find nodes that have port information
                                    portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                                    for pn in portNodes:
                                        # create port
                                        port = Port()
                                        port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                        port.name = pn.get("Name")
                                        # x coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                        # y coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                        
                                        junc.ports.append(port)
                                    hmi.juncts.append(junc)
                                elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/Connection/MeasurementLine":
                                    # add measurement line objects
                                    measLinObj = Line()
                                    measLinObj.type = "Measurement Line"
                                    measLinObj.name = gchild.get("Name")
                                    # edge path
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value") is not None:
                                        measLinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue") is not None:
                                        measLinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue")
                                    
                                    # find nodes that have port information
                                    portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/MeasurementPoint']")
                                    for pn in portNodes:
                                        # create port
                                        port = Port()
                                        port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                        port.name = pn.get("Name")
                                        # x coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                        # y coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                        
                                        measLinObj.ports.append(port)
                                    hmi.lines.append(measLinObj)
                                elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/Connection/FunctionLine":
                                    # add function line objects
                                    functlinObj = Line()
                                    functlinObj.type = "Function Line"
                                    functlinObj.name = gchild.get("Name")
                                    # edge path
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value") is not None:
                                        functlinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue") is not None:
                                        functlinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue")
                                    
                                    # find nodes that have port information
                                    portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/LogicalPort']")
                                    for pn in portNodes:
                                        # create port
                                        port = Port()
                                        port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                        port.name = pn.get("Name")
                                        # x coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                        # y coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                        
                                        functlinObj.ports.append(port)
                                    hmi.lines.append(functlinObj)
                                elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/Connection/Pipe":
                                    # add pipe objects
                                    pipeObj = Pipe()
                                    pipeObj.name = gchild.get("Name")
                                    # directed flag
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}Value") is not None:
                                        pipeObj.direct = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}DefaultValue") is not None:
                                        pipeObj.direct = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}DefaultValue")
                                    # edge path
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value") is not None:
                                        pipeObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue") is not None:
                                        pipeObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue")
                                    
                                    # find nodes that have port information
                                    portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                                    for pn in portNodes:
                                        # create port
                                        port = Port()
                                        port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                        port.name = pn.get("Name")
                                        # x coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                        # y coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                        
                                        pipeObj.ports.append(port)
                                    hmi.pipes.append(pipeObj)
                                elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/VisualObject":
                                    # add visual objects
                                    visObj = VisualObject()
                                    visObj.name = gchild.get("Name")
                                    # width
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}Value") is not None:
                                        visObj.width = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.width = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}DefaultValue")
                                    # height
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}Value") is not None:
                                        visObj.height = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.height = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}DefaultValue")
                                    # x coordinate
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                        visObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                    # y coordinate
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                        visObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                    # z index
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value") is not None:
                                        visObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue")
                                    # rotation
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}Value") is not None:
                                        visObj.rotation = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.rotation = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}DefaultValue")
                                    # eClass Version
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}Value") is not None:
                                        visObj.eClassVer = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.eClassVer = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}DefaultValue")
                                    # eClass Classification Class
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}Value") is not None:
                                        visObj.eClassClass = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.eClassClass = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}DefaultValue")
                                    # eClass IRDI
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}Value") is not None:
                                        visObj.eClassIRDI = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.eClassIRDI = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}DefaultValue")
                                    # refId
                                    if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value") is not None:
                                        visObj.refId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value")
                                    elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}DefaultValue") is not None:
                                        visObj.refId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}DefaultValue")
                                    # refInstance
                                    visObj.refInst = mtp.getInstance(instId=visObj.refId)
                                    
                                    # find nodes that have port information
                                    portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                                    for pn in portNodes:
                                        # create port
                                        port = Port()
                                        port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                        port.name = pn.get("Name")
                                        # x coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                            port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                        # y coordinate
                                        if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                        elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                            port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                        
                                        visObj.ports.append(port)
                                    hmi.visuals.append(visObj)
                                elif gchild.tag == f"{NAMESPACE}InternalLink":
                                    sideA = gchild.get("RefPartnerSideA")
                                    sideB = gchild.get("RefPartnerSideB")
                                    hmi.links.append((sideA, sideB))

                            mtp.hmis.append(hmi)
            elif child.tag == f"{NAMESPACE}InstanceHierarchy" and child.get("Name") == "Pictures":
                # parse HMI Information for HC30
                hminode = child.find(f".//*[@RefBaseSystemUnitPath='MTPHMISUCLib/Picture'][@Name='{mtp.name}']")
                # create hmi
                hmi = HMI()
                # set type to RI because HC30 doesn't support services
                hmi.type = "RI"
                for gchild in hminode:
                    if gchild.tag == f"{NAMESPACE}Attribute":
                        if gchild.get("Name") == "Width":
                            if int(gchild.findtext(f"{NAMESPACE}Value")) is not None:
                                hmi.width = int(gchild.findtext(f"{NAMESPACE}Value"))
                            elif int(gchild.findtext(f"{NAMESPACE}DefaultValue")) is not None:
                                hmi.width = int(gchild.findtext(f"{NAMESPACE}DefaultValue"))
                        elif gchild.get("Name") == "Height":
                            if int(gchild.findtext(f"{NAMESPACE}Value")) is not None:
                                hmi.height = int(gchild.findtext(f"{NAMESPACE}Value"))
                            elif int(gchild.findtext(f"{NAMESPACE}DefaultValue")) is not None:
                                hmi.height = int(gchild.findtext(f"{NAMESPACE}DefaultValue"))
                        elif gchild.get("Name") == "HierarchyLevel":
                            if gchild.findtext(f"{NAMESPACE}Value") is not None:
                                hmi.hierarchy = gchild.findtext(f"{NAMESPACE}Value")
                            elif gchild.findtext(f"{NAMESPACE}DefaultValue") is not None:
                                hmi.hierarchy = gchild.findtext(f"{NAMESPACE}DefaultValue")
                    elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/Connection/MeasurementLine":
                        # add measurement line objects
                        measLinObj = Line()
                        measLinObj.type = "Measurement Line"
                        measLinObj.name = gchild.get("Name")
                        # edge path
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value") is not None:
                            measLinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue") is not None:
                            measLinObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue")
                        # z index
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value") is not None:
                            measLinObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue") is not None:
                            measLinObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue")
                        
                        # find nodes that have port information
                        portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/MeasurementPoint']")
                        for pn in portNodes:
                            # create port
                            port = Port()
                            port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                            port.name = pn.get("Name")
                            # x coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                            
                            measLinObj.ports.append(port)
                        hmi.lines.append(measLinObj)
                    elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/Connection/Pipe":
                        # add pipe objects
                        pipeObj = Pipe()
                        pipeObj.name = gchild.get("Name")
                        # directed flag
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}Value") is not None:
                            pipeObj.direct = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}DefaultValue") is not None:
                            pipeObj.direct = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Directed']/{NAMESPACE}DefaultValue")
                        # edge path
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value") is not None:
                            pipeObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue") is not None:
                            pipeObj.ep = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Edgepath']/{NAMESPACE}DefaultValue")
                        # z Index
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value") is not None:
                            pipeObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue") is not None:
                            pipeObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue")
                        
                        # find nodes that have port information
                        portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                        for pn in portNodes:
                            # create port
                            port = Port()
                            port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                            port.name = pn.get("Name")
                            # x coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                            
                            pipeObj.ports.append(port)
                        hmi.pipes.append(pipeObj)
                    elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/VisualObject":
                        # add visual objects
                        visObj = VisualObject()
                        visObj.name = gchild.get("Name")
                        # width
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}Value") is not None:
                            visObj.width = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}DefaultValue") is not None:
                            visObj.width = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Width']/{NAMESPACE}DefaultValue")
                        # height
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}Value") is not None:
                            visObj.height = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}DefaultValue") is not None:
                            visObj.height = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Height']/{NAMESPACE}DefaultValue")
                        # x coordinate
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                            visObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                            visObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                        # y coordinate
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                            visObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                            visObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                        # z index
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value") is not None:
                            visObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue") is not None:
                            visObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue")
                        # rotation
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}Value") is not None:
                            visObj.rotation = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}DefaultValue") is not None:
                            visObj.rotation = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Rotation']/{NAMESPACE}DefaultValue")
                        # eClass Version
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}Value") is not None:
                            visObj.eClassVer = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}DefaultValue") is not None:
                            visObj.eClassVer = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassVersion']/{NAMESPACE}DefaultValue")
                        # eClass Classification Class
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}Value") is not None:
                            visObj.eClassClass = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}DefaultValue") is not None:
                            visObj.eClassClass = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassClassificationClass']/{NAMESPACE}DefaultValue")
                        # eClass IRDI
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}Value") is not None:
                            visObj.eClassIRDI = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}DefaultValue") is not None:
                            visObj.eClassIRDI = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='eClassIRDI']/{NAMESPACE}DefaultValue")
                        # refId
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value") is not None:
                            visObj.refId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}DefaultValue") is not None:
                            visObj.refId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='RefID']/{NAMESPACE}DefaultValue")
                        # refInstance
                        visObj.refInst = mtp.getInstance(instId=visObj.refId)

                        # find nodes that have port information
                        portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                        for pn in portNodes:
                            # create port
                            port = Port()
                            port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                            port.name = pn.get("Name")
                            # x coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")

                            visObj.ports.append(port)
                        hmi.visuals.append(visObj)
                    elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/TopologyObject/Termination/Source":
                        # add source objects
                        sourceObj = Source()
                        sourceObj.name = gchild.get("Name")
                        # x coordinate
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                            sourceObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                            sourceObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                        # y coordinate
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                            sourceObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                            sourceObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                        # z index
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value") is not None:
                            sourceObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue") is not None:
                            sourceObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue")
                        # term ID
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value") is not None:
                            sourceObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue") is not None:
                            sourceObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue")
                        
                        # find nodes that have port information
                        portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                        for pn in portNodes:
                            # create port
                            port = Port()
                            port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                            port.name = pn.get("Name")
                            # x coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                            
                            sourceObj.ports.append(port)
                        hmi.srcs.append(sourceObj)
                    elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/TopologyObject/Termination/Sink":
                        # add sink objects
                        sinkObj = Sink()
                        sinkObj.name = gchild.get("Name")
                        # x coordinate
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                            sinkObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                            sinkObj.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                        # y coordinate
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                            sinkObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                            sinkObj.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                        # z index
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value") is not None:
                            sinkObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue") is not None:
                            sinkObj.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue")
                        # term ID
                        if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value") is not None:
                            sinkObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}Value")
                        elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue") is not None:
                            sinkObj.termId = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='TermID']/{NAMESPACE}DefaultValue")
                        
                        # find nodes that have port information
                        portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                        for pn in portNodes:
                            # create port
                            port = Port()
                            port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                            port.name = pn.get("Name")
                            # x coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                            
                            sinkObj.ports.append(port)
                        hmi.sinks.append(sinkObj)
                    elif gchild.tag == f"{NAMESPACE}InternalElement" and gchild.get("RefBaseSystemUnitPath") == "MTPHMISUCLib/TopologyObject/Junction":
                            # add junction objects
                            junc = Junction()
                            junc.name = gchild.get("Name")
                            # x coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                junc.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                junc.x = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                            # y coordinate
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                junc.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                junc.y = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                            # z index
                            if gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value") is not None:
                                junc.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}Value")
                            elif gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue") is not None:
                                junc.zindex = gchild.findtext(f".//{NAMESPACE}Attribute[@Name='ZIndex']/{NAMESPACE}DefaultValue")

                            # find nodes that have port information
                            portNodes = gchild.findall(f".//{NAMESPACE}InternalElement[@RefBaseSystemUnitPath='MTPHMISUCLib/PortObject/Nozzle']")
                            for pn in portNodes:
                                # create port
                                port = Port()
                                port.connectId = pn.find(f".//{NAMESPACE}ExternalInterface[@Name='Connector']").get("ID")
                                port.name = pn.get("Name")
                                # x coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue") is not None:
                                    port.x = pn.findtext(f".//{NAMESPACE}Attribute[@Name='X']/{NAMESPACE}DefaultValue")
                                # y coordinate
                                if pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}Value")
                                elif pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue") is not None:
                                    port.y = pn.findtext(f".//{NAMESPACE}Attribute[@Name='Y']/{NAMESPACE}DefaultValue")
                                
                                junc.ports.append(port)
                            hmi.juncts.append(junc)

                mtp.hmis.append(hmi)
        # get sensors and actuators
        for i in mtp.insts:
            if not (mtp.hasParameter(i.id) or mtp.hasProcedure(i.id) or mtp.hasService(i.id) or i.name == "PeaInforamtionLabel"):
                mtp.sensacts.append(i)
        


    # debugging only
    for m in mtps:
        print(m.name)
        for s in m.servs:
            print(s.name, s.id)
            for p in s.procs:
                print("  ", p.name, p.id)
                for pa in p.params:
                    print("    ", pa.name, pa.id, pa.default, pa.unit)
            print("\n")

    ## debugging only
    # print("Services: ")
    # for s in mtp.servs:
    #     print(s.name)
    # print("\n", "Procedures: ")
    # for p in mtp.procs:
    #     print(p.name)
    # print("\n", "Sensors and Actuators: ")
    # for sa in mtp.sensacts:
    #     if sa.paramElem["V"]["ID"] is not None:
    #         print(sa.name, sa.paramElem["V"]["ID"])
    #     elif sa.paramElem["VOut"]["ID"] is not None:
    #         print(sa.name, sa.paramElem["VOut"]["ID"])
    #     elif sa.paramElem["Pos"]["ID"] is not None:
    #         print(sa.name, sa.paramElem["Pos"]["ID"])
    #     elif sa.paramElem["Ctrl"]["ID"] is not None:
    #         print(sa.name, sa.paramElem["Ctrl"]["ID"])

    return mtps

if __name__ == "__main__":
    getMtps(input_files=None, logger=None)