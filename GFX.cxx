#include <iostream>
#include <vector>
#include <cmath>

// Constants
const int numParticles = 1000; // Number of particles
const float dt = 0.01f; // Time step
const float h = 0.05f; // Smoothing length
const float mass = 0.02f; // Particle mass
const float density0 = 1000.0f; // Reference density
const float stiffness = 1000.0f; // Gas stiffness
const float viscosity = 0.1f; // Viscosity coefficient

// Particle structure
struct Particle {
    float x, y; // Position
    float vx, vy; // Velocity
    float density; // Density
    float pressure; // Pressure
};

// Function to initialize particles
void initializeParticles(std::vector<Particle>& particles) {
    for (int i = 0; i < numParticles; ++i) {
        Particle p;
        p.x = static_cast<float>(rand()) / RAND_MAX; // Random position between 0 and 1
        p.y = static_cast<float>(rand()) / RAND_MAX;
        p.vx = 0.0f;
        p.vy = 0.0f;
        p.density = 0.0f;
        p.pressure = 0.0f;
        particles.push_back(p);
    }
}

// Function to compute density and pressure of particles
void computeDensityPressure(std::vector<Particle>& particles) {
    for (auto& p1 : particles) {
        p1.density = 0.0f;
        for (const auto& p2 : particles) {
            float dx = p2.x - p1.x;
            float dy = p2.y - p1.y;
            float r2 = dx * dx + dy * dy;
            if (r2 < h * h) {
                p1.density += mass * (315.0f / (64.0f * M_PI * std::pow(h, 9))) * std::pow(h * h - r2, 3);
            }
        }
        p1.pressure = stiffness * (p1.density - density0);
    }
}

// Function to compute forces on particles
void computeForces(std::vector<Particle>& particles) {
    for (auto& p1 : particles) {
        float pressureForceX = 0.0f;
        float pressureForceY = 0.0f;
        float viscosityForceX = 0.0f;
        float viscosityForceY = 0.0f;
        for (const auto& p2 : particles) {
            if (&p1 != &p2) {
                float dx = p2.x - p1.x;
                float dy = p2.y - p1.y;
                float r = std::sqrt(dx * dx + dy * dy);
                if (r < h) {
                    // Pressure force
                    pressureForceX += -mass * (p1.pressure / (p1.density * p1.density) + p2.pressure / (p2.density * p2.density)) * (dx / r) * (315.0f / (64.0f * M_PI * std::pow(h, 9))) * std::pow(h * h - r * r, 2);
                    pressureForceY += -mass * (p1.pressure / (p1.density * p1.density) + p2.pressure / (p2.density * p2.density)) * (dy / r) * (315.0f / (64.0f * M_PI * std::pow(h, 9))) * std::pow(h * h - r * r, 2);

                    // Viscosity force
                    viscosityForceX += viscosity * mass * (p2.vx - p1.vx) / p2.density * (45.0f / (M_PI * std::pow(h, 6))) * (h - r);
                    viscosityForceY += viscosity * mass * (p2.vy - p1.vy) / p2.density * (45.0f / (M_PI * std::pow(h, 6))) * (h - r);
                }
            }
        }
        p1.vx += (pressureForceX + viscosityForceX) * dt;
        p1.vy += (pressureForceY + viscosityForceY) * dt;
    }
}

// Function to integrate particle motion
void integrateMotion(std::vector<Particle>& particles) {
    for (auto& p : particles) {
        p.x += p.vx * dt;
        p.y += p.vy * dt;
    }
}

// Function to output particle positions
void outputParticlePositions
(std::vector<Particle>& particles) {
    for (const auto& p : particles) {
        std::cout << "Particle Position: (" << p.x << ", " << p.y << ")" << std::endl;
    }
}

int main() {
    // Initialize particles
    std::vector<Particle> particles;
    initializeParticles(particles);

    // Main simulation loop
    for (int step = 0; step < 1000; ++step) {
        // Step 1: Compute density and pressure
        computeDensityPressure(particles);

        // Step 2: Compute forces
        computeForces(particles);

        // Step 3: Integrate motion
        integrateMotion(particles);

        // Step 4: Output particle positions (for visualization)
        outputParticlePositions(particles);
    }

    return 0;
}

