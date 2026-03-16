public class MainAula {
    public static void main(String[] args) {
        String[][] datos = {
                {"Luis", "67"},
                {"Aracely", "89"},
                {"Juan", "34"},
                {"Marisol", "45"},
        };
        Aula a1 = new Aula("Aula 1", 1, datos);
        a1.mostrar();
        System.out.println("situacion de los estudiantes:");
        a1.mostrar("situacion");
    }
}