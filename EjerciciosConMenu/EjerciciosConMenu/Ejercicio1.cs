using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EjerciciosConMenu
{
    public class Ejercicio1
    {
        public void Ejecutar()
        {
            Console.WriteLine("Ejercicio 1: Calcular área en manzanas");
            double longitud;
            Console.Write("Ingrese la longitud del terreno en varas: ");
            while (!double.TryParse(Console.ReadLine(), out longitud) || longitud <= 0)
            {
                Console.Write("Dato inválido. Ingrese un número positivo: ");
            }

            double ancho = 5;
            double areaVaras = longitud * ancho;
            double areaManzanas = areaVaras / 1428.8;

            Console.WriteLine("El área total es: " + areaManzanas.ToString("F4") + " manzanas");
        }
    }
}
