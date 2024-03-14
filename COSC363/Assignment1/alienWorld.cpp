#include <iostream>
#include <fstream>
#include <GL/freeglut.h>
#include <climits>
#include <cmath>
using namespace std;

float camX = 0, camY = 5, camZ = 0;
float angle = 0;

void drawFloor()
{
    glColor3f(0., 0.5, 0.);

    for (int i = -50; i <= 50; i++)
    {
        glBegin(GL_LINES);
            glVertex3f(-50, -0.75, i);
            glVertex3f(50, -0.75, i);
            glVertex3f(i, -0.75, -50);
            glVertex3f(i, -0.75, 50);
        glEnd();
    }
}

void display()
{
    float lpos[4] = {0., 10., 10., 1.0};

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    float lx = sin((angle / 180) * M_PI);
    float lz = -cos((angle / 180) * M_PI);

    gluLookAt(camX, camY, camZ, camX + lx, camY, camZ + lz, 0, 1, 0);

    glLightfv(GL_LIGHT0, GL_POSITION, lpos);

    glRotatef(angle, 0.0, 1.0, 0.0);
    glDisable(GL_LIGHTING);
    drawFloor();

    glEnable(GL_LIGHTING);

    glFlush();
}

void initialize()
{
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_NORMALIZE);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(50, 1, 10.0, 1000.0);
}

void special(int key, int x, int y) {
    float angleRadians = (angle / 180) * M_PI;
    float forwardX = sin(angleRadians);
    float forwardZ = -cos(angleRadians);

    switch (key) {
        case GLUT_KEY_LEFT:
            angle -= 5.0;
            break;
        case GLUT_KEY_RIGHT:
            angle += 5.0;
            break;
        case GLUT_KEY_UP:
            camX += forwardX;
            camZ += forwardZ;
            break;
        case GLUT_KEY_DOWN:
            camX -= forwardX;
            camZ -= forwardZ;
            break;
    }
    if (angle > 360) angle -= 360;
    if (angle < 0) angle += 360;

    glutPostRedisplay();
}


void keyboard(unsigned char key, int x, int y)
{

}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH);
    glutInitWindowSize(800, 800);
    glutInitWindowPosition(10, 10);
    glutCreateWindow("Alien World");
    initialize();

    glutDisplayFunc(display);
    glutSpecialFunc(special);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
    return 0;
}
