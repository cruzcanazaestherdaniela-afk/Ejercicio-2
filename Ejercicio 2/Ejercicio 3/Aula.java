public class Aula {
    String nombreAula;
    int piso;
    String[][] estudiantes;
    public Aula(String nombreAula, int piso, String[][] estudiantes) {
        this.nombreAula = nombreAula;
        this.piso = piso;
        this.estudiantes = estudiantes;
    }
    public void mostrar() {
        System.out.println("Aula: " + nombreAula);
        System.out.println("Piso: " + piso);
        for (int i = 0; i < estudiantes.length; i++) {
            System.out.println(estudiantes[i][0]  +" "+ estudiantes[i][1]);
        }
    }
    public void mostrar(String situacion) {
        for (int i = 0; i < estudiantes.length; i++) {
            int nota = Integer.parseInt(estudiantes[i][1]);
            if (nota >= 51) {
                System.out.println(estudiantes[i][0] + " APROBADO");
            }
            else {
                System.out.println(estudiantes[i][0] + " REPROBADO");
            }
        }
    }
}