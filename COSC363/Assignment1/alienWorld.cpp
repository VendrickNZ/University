#include <iostream>
#include <fstream>
#include <GL/freeglut.h>
#include <climits>
#include <cmath>
using namespace std;


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

    gluLookAt(0, 5, 0, 0, 6, -1, 0, 1, 0);

    glLightfv(GL_LIGHT0, GL_POSITION, lpos);

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

void special(int key, int x, int y)
{

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
