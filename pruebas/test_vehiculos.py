import unittest
import vehiculos

class TestVehiculos(unittest.TestCase):
    def test_existencia_vehiculo(self):
        v = vehiculos.Vehiculo()
        self.assertIsNotNone(v)

    def test_existencia_atributos(self):
        t = vehiculos.Vehiculo("coche", 60, 3000)
        self.assertEqual(t.kilometraje, 3000)
        self.assertEqual(t.nombre, "coche")
        self.assertEqual(t.velocidad_maxima, 60)  

    def test_todos_vehiculos_color_blanco(self):
        
        resp = vehiculos.Vehiculo.color
        self.assertEqual(resp, 'blanco')

class TestBus(unittest.TestCase):
    def test_existencia_bus(self):
        b = vehiculos.Bus('Toyota',80,2000)
        self.assertEqual(b.kilometraje, 2000)
        self.assertEqual(b.nombre, "Toyota")
        self.assertEqual(b.velocidad_maxima, 80)

    def test_existencia_atributo_capacidad(self):
        b = vehiculos.Bus('Toyota',80,2000)
        b.set_capacidad(150)
        capa_b = b.capacidad
        # vehiculos.Vehiculo.color = 'amarillo'
        # c = vehiculos.Vehiculo()
        self.assertEqual(capa_b,150)
        self.assertEqual(b.color, 'blanco')
