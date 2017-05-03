def datoPersonal():
error=0
comparador(titularPdf, titularBdd) comparador(direccionPdf, direccionBdd) if error > 0:
print("error datos personales")
def comparador(valorPdf, valorBdd): error=0
valorPdf= valorPdf.strip()
valorBdd= valorBdd.strip()
if valorPdf != valorBdd:
print('error=si')
error=error+1
titularPdf = 'antonio'
titularBdd = 'antonio '
direccionPdf = 'san cugat' direccionBdd = 'malaga'
print(titularBdd) datoPersonal()
