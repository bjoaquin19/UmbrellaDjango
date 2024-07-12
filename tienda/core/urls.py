from django.urls import path
from .views import index, poblar, ficha, ingresar, nosotros, registrarme, bodega, misdatos, mipassword, miscompras,salir
from .views import ropa, administracion, boleta, productos, comprar_ahora
from .views import agregar_producto_al_carrito, usuarios, eliminar_producto_en_bodega
from .views import obtener_productos, ventas, cambiar_estado_boleta, carrito
from .views import eliminar_producto_en_carrito, vaciar_carrito
from .views import vaciar_carrito, mipassword, cambiar_password

# from .views import registrarme, nosotros, admin_productos, admin_usuarios, admin_bodega, ventas, boleta, ingresar, admin_usuarios
# from .views import misdatos, miscompras, salir, carrito, ficha
# from .views import cambiar_estado_boleta, poblar, obtener_productos, eliminar_producto_en_bodega
# from .views import premio, eliminar_producto_en_carrito, agregar_producto_al_carrito


urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('poblar_db/', poblar, name='poblar_db'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    path('ingresar', ingresar, name='ingresar'),
    path('nosotros', nosotros, name='nosotros'),
    path('registrarme', registrarme, name='registrarme'),
    path('ropa', ropa, name='ropa'),
    path('administracion', administracion, name='administracion'),
    path('boleta/<nro_boleta>', boleta, name='boleta'),
    path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),
    path('obtener_productos', obtener_productos, name='obtener_productos'),
    path('producto/<accion>/<id>', productos, name='productos'),
    path('usuarios/<accion>/<id>', usuarios, name='usuarios'),
    path('comprar_ahora', comprar_ahora, name='comprar_ahora'),
    path('agregar_producto_al_carrito/<producto_id>', agregar_producto_al_carrito, name='agregar_producto_al_carrito'),
    path('carrito', carrito, name='carrito'),
    path('admin_bodega', bodega, name='admin_bodega'),
    path('misdatos', misdatos, name='misdatos'),
    path('mipassword', mipassword, name='mipassword'),
    path('miscompras', miscompras, name='miscompras'),
    path('salir', salir, name='salir'),
    path('ventas', ventas, name='ventas'),
    path('cambiar_estado_boleta/<nro_boleta>/<estado>', cambiar_estado_boleta, name='cambiar_estado_boleta'),
    path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    path('vaciar_carrito', vaciar_carrito, name='vaciar_carrito'),
    path('cambiar_password', cambiar_password, name='cambiar_password'),


    # path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),
    # 
    # path('carrito', carrito, name='carrito'),
    # path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    # path('vaciar_carrito', vaciar_carrito, name='vaciar_carrito'),
]