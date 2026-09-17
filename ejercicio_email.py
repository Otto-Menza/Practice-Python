# Crear un correo usando las herramientas y metodos vistos aceca de cadenas.
nombre = 'Ubaldo Acosta Soto'
empresa = 'Global Mentoring'
dominio = '.com.mx'
arroba = '@'

print(f'Nombre de usuario: {nombre}')
nombre_normalizado = nombre.lower().replace(' ','.')
print(f'Nombre de usuario normalizado: {nombre_normalizado}')

print(f'Nombre de empresa: {empresa}')
empresa_normalizado = empresa.lower().replace(' ','')
print(f'Nombre de empresa normalizado: {empresa_normalizado}')
email = ''.join([nombre_normalizado,arroba,empresa_normalizado,dominio])
print(f'Email final generado: {email}')