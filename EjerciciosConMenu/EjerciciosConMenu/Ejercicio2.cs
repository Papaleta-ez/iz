using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EjerciciosConMenu
{
    public class Ejercicio2
    {
        public void Ejecutar()
        {
            Console.WriteLine("Ejercicio 2: Tiempo de viaje Managua - Granada");
            double velocidad;
            Console.Write("Ingrese la velocidad promedio en km/h: ");
            while (!double.TryParse(Console.ReadLine(), out velocidad) || velocidad <= 0)
            {
                Console.Write("Dato inválido. Ingrese un número mayor a 0: ");
            }

            double distancia = 40;
            double tiempo = distancia / velocidad;

            Console.WriteLine("El tiempo estimado es: " + tiempo.ToString("F2") + " horas");
        }
    }
}
