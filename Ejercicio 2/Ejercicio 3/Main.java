import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Videojuegos juego1 = new Videojuegos("Mario Kart", "PC");
        juego1.agregarJugadores();
        System.out.print("Ingrese cantidad de jugadores a agregar: ");
        int cantidad = sc.nextInt();
        juego1.agregarJugadores(cantidad);
        juego1.mostrar();
    }
}