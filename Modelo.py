class ActivoBuilder:
    def __init__(self):
        self._caja = None
        self._bancos = None
        self._mercaderias = None
        self._materiasprimas = None
        self._clientes = None
        self._deudores = None
        self._creditocortoplazenaj = None
        self._terrenos = None
        self._construcciones = None
        self._maquinaria = None
        self._mobiliario = None
        self._elementosdetransporte = None
        self._creditolargoplazoenaj = None
    def set_caja(self,caja):
        self._caja = caja
        return self
    def set_bancos(self,bancos):
        self._bancos = bancos
        return self
    def set_mercaderias(self,mercaderias):
        self._mercaderias = mercaderias
        return self
    def set_materiasprimas(self,materiasprimas):
        self._materiasprimas = materiasprimas
        return self
    def set_clientes(self,clientes):
        self._clientes = clientes
        return self
    def set_deudores(self,deudores):
        self._deudores = deudores
        return self
    def set_creditocortoplazenaj(self,creditocortoplazenaj):
        self._creditocortoplazenaj = creditocortoplazenaj):
        return self
    def set_terrenos(self,terrenos):
        self._terrenos=terrenos
        return self
    def set_construcciones(self,construcciones):
        self._construcciones = construcciones
        return self
    def set_maquinaria(self,maquinaria):
        self._maquinaria = maquinaria
        return self
    def set_mobiliario(self,mobiliario):
        self._mobiliario = mobiliario    
        return self
    def elementosdetransporte(self,elementosdetransporte):
        self._elementosdetransporte = elementosdetransporte
        return self
    def creditolargoplazoenaj(self,creditolargoplazoenaj):
        self._creditolargoplazoenaj
        return self
    def build(self):
        return Activo(self.cajas,self.bancos,self.mercaderias,self.materiasprimas,self.clientes,self.deudores,self.creditocortoplazenaj,self.terrenos,self.construcciones,self.maquinaria,self.mobiliario,self.elementosdetransporte,self.creditolargoplazoenaj)
class Activo:
    def __init__(self,cajas=None,bancos=None,mercaderias=None,materiasprimas=None,clientes=None,deudores=None,creditocortoplazenaj=None,terrenos=None,construcciones=None,maquinaria=None,mobiliario=None,elementosdetransporte=None,creditolargoplazoenaj=None):


        self.importe = cajas + bancos + mercaderias + materiasprimas + clientes  deudores + creditocortoplazenaj + terrenos + construcciones + maquinaria + mobiliario + elementosdetransporte + creditolargoplazoenaj 
        self.cajas = cajas
        self.bancos = bancos
        self.mercaderias = mercaderias
        self.materiasprimas = materiasprimas
        self.clientes = clientes
        self.deudores = deudores
        self.cortoplazenaj = cortoplazenaj
        self.terrenos = construcciones
        self.maquinaria = maquinaria
        self.mobiliario = mobiliario
        self.elementosdetransporte = elementosdetransporte
        self.creditolargoplazoenaj = creditolargoplazoenaj

class PasivoBuilder:
    def __init__(self):
        self._importe = None
        self._nocorriente = None
        self._corriente = None
        self._noexigible = None
        self._proveedores = None
        self._efectoscomerciales = None
        self._acreedores = None
        self._inmovilizadocortoplazo = None
        self._deudasbanco = None
        self._inmovilizadolargoplazo = None
        self._deudasbancolargoplazo = None

    def set_nocorriente(self,nocorriente):
        self._nocorriente = nocorriente
        return self
    def set_corriente(self,corriente):
        self._corriente = corriente
        return self
    def set_noexigible(self,noexigible):
        self._noexigible = noexigible
        return self
    def set_proveedores(self,proveedores):
        self._proveedores = proveedores
        return self
    def set_efectoscomerciales(self,efectoscomerciales):
        self._efectoscomerciales = efectoscomerciales
        return self
    def set_acreedores(self,acreedores):
        self._acreedores = acreedores
        return self
    def set_inmovilizadocortoplazo(self,inmovilizadocortoplazo):
        self._inmovilizadocortoplazo = inmovilizadocortoplazo
        return self
    def set_deudasbanco(self,deudasbanco):
        self._deudasbanco = deudasbanco
        return self
    def set_inmovilizadolargoplazo(self,inmovilizadolargoplazo):
        self._inmovilizadolargoplazo = inmovilizadolargoplazo
        return self
    def set_deudasbancolargoplazo(self, deudasbancolargoplazo):
        self._deudasbancolargoplazo = deudasbancolargoplazo
        return self

    def build(self):
        return Pasivo(nocorriente,corriente,noexigible,proveedores,efectoscormerciales,acreedores,inmovilizadocortoplazo,deudasbanco,inmovilizadolargoplazo,deudasbancolargoplazo)
class Pasivo:
    def __init__(self, nocorriente=None,corriente=None,noexigible=None,proveedores=None,efectoscomerciales=None,acreedores=None,inmovilizadocortoplazo=None,deudasbanco=None,inmovilizadolargoplazo=None,deudasbancolargoplazo=None):
        self.importe = corriente + nocorriente
        self.nocorriente = nocorriente
        self.corriente = corriente
        self.noexigible = noexigible
        self.proveedores = proveedores
        self.efectoscomerciales = efectoscomerciales
        self.acreedores = acreedores
        self.inmovilizadocortoplazo = inmovilizadocortoplazo
        self.deudasbanco = deudasbanco
        self.inmovilizadolargoplazo = inmovilizadoolargoplazo
        self.deudasbancolargoplazo = deudasbancolargoplazo
class Patrimonioneto:
    def __init__(self,activo,pasivo):
        self.importe=activo-pasivo

class Balance:
    def __init__(self, activo, pasivo):
        # Este es el constructor. Se llama automáticamente cuando se crea una instancia.
        # Los atributos nombre y edad se inicializan aquí.
        self.activo = activo
        self.pasivo = pasivo
        self.patrimonioneto= activo - pasivo

class Hechocontable:
    def __init__(self,activo,pasivo):
        self.activo=activo
        self.pasivo=pasivo
        self.patrimonioneto=self.activo-self.pasivo



