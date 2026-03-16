public class Videojuegos {
    String nombre;
    String plataforma;
    int jugadores;
    public Videojuegos(String nombre, String plataforma) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.jugadores = 0;
    }
    public void agregarJugadores() {
        jugadores=jugadores+1;
    }
    public void agregarJugadores(int cantidad) {
        jugadores = jugadores + cantidad;
    }
    public void mostrar() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Plataforma: " + plataforma);
        System.out.println("Jugadores: " + jugadores);
    }
}