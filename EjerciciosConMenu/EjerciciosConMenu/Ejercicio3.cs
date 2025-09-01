using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EjerciciosConMenu
{
    public class Ejercicio3
    {
        public void Ejecutar()
        {
            Console.WriteLine("Ejercicio 3: Distancia recorrida ciclista");
            double velocidad, tiempo;

            Console.Write("Ingrese la velocidad promedio en km/h: ");
            while (!double.TryParse(Console.ReadLine(), out velocidad) || velocidad <= 0)
            {
                Console.Write("Dato inválido. Ingrese un número mayor a 0: ");
            }

            Console.Write("Ingrese el tiempo recorrido en horas: ");
            while (!double.TryParse(Console.ReadLine(), out tiempo) || tiempo <= 0)
            {
                Console.Write("Dato inválido. Ingrese un número mayor a 0: ");
            }

            double distancia = velocidad * tiempo;
            Console.WriteLine("La distancia total recorrida es: " + distancia.ToString("F2") + " km");
        }
    }
}
