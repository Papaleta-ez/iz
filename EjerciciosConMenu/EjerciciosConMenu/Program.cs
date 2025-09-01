using System;

namespace EjerciciosConMenu
{
    class Program
    {
        static void Main(string[] args)
        {
            bool salir = false;

            while (!salir)
            {
                Console.Clear();
                Console.WriteLine("=== MENÚ DE EJERCICIOS ===");
                Console.WriteLine("1. Área en manzanas");
                Console.WriteLine("2. Tiempo de viaje Managua - Granada");
                Console.WriteLine("3. Distancia ciclista");
                Console.WriteLine("4. Volumen de agua en tanque");
                Console.WriteLine("5. Producción de leche");
                Console.WriteLine("0. Salir");
                Console.Write("Seleccione una opción: ");

                string opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1":
                        new Ejercicio1().Ejecutar();
                        break;
                    case "2":
                        new Ejercicio2().Ejecutar();
                        break;
                    case "3":
                        new Ejercicio3().Ejecutar();
                        break;
                    case "4":
                        new Ejercicio4().Ejecutar();
                        break;
                    case "5":
                        new Ejercicio5().Ejecutar();
                        break;
                    case "0":
                        salir = true;
                        break;
                    default:
                        Console.WriteLine("Opción inválida. Intente de nuevo.");
                        break;
                }

                if (!salir)
                {
                    Console.WriteLine("\nPresione una tecla para volver al menú...");
                    Console.ReadKey();
                }
            }
        }
    }
}
