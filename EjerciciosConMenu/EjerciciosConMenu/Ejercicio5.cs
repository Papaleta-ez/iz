using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EjerciciosConMenu
{
    public class Ejercicio5
    {
        public void Ejecutar()
        {
            Console.WriteLine("Ejercicio 5: Producción de leche");
            double litrosPorVaca;
            int numeroVacas;

            Console.Write("Ingrese el volumen promedio de leche por vaca en litros: ");
            while (!double.TryParse(Console.ReadLine(), out litrosPorVaca) || litrosPorVaca <= 0)
            {
                Console.Write("Dato inválido. Ingrese un número mayor a 0: ");
            }

            Console.Write("Ingrese el número total de vacas ordeñadas: ");
            while (!int.TryParse(Console.ReadLine(), out numeroVacas) || numeroVacas <= 0)
            {
                Console.Write("Dato inválido. Ingrese un número entero mayor a 0: ");
            }

            double litrosTotales = litrosPorVaca * numeroVacas;
            double baldes = litrosTotales / 20.0;

            Console.WriteLine("La producción total es: " + baldes.ToString("F2") + " baldes de leche");
        }
    }
}
