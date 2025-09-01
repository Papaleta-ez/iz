using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EjerciciosConMenu
{
    public class Ejercicio4
    {
        public void Ejecutar()
        {
            Console.WriteLine("Ejercicio 4: Volumen de agua en un tanque");
            double longitud, ancho, altura;

            Console.Write("Ingrese la longitud del tanque en metros: ");
            while (!double.TryParse(Console.ReadLine(), out longitud) || longitud <= 0)
            {
                Console.Write("Dato inválido. Ingrese un número mayor a 0: ");
            }

            Console.Write("Ingrese el ancho del tanque en metros: ");
            while (!double.TryParse(Console.ReadLine(), out ancho) || ancho <= 0)
            {
                Console.Write("Dato inválido. Ingrese un número mayor a 0: ");
            }

            Console.Write("Ingrese la altura del tanque en metros: ");
            while (!double.TryParse(Console.ReadLine(), out altura) || altura <= 0)
            {
                Console.Write("Dato inválido. Ingrese un número mayor a 0: ");
            }

            double volumen = longitud * ancho * altura;
            Console.WriteLine("El volumen total del tanque es: " + volumen.ToString("F2") + " m³");
        }
    }
}
