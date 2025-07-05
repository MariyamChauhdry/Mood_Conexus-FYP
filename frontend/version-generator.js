import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';

// Get current directory path
const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Create require function for ES module
const require = createRequire(import.meta.url);

// Synchronous version checker
const getVersionSync = (pkg) => {
  try {
    const pkgPath = path.join(process.cwd(), 'node_modules', pkg, 'package.json');
    const pkgJson = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
    return pkgJson.version;
  } catch (error) {
    return 'not-installed';
  }
};

// Get versions
const nodeVersion = process.version.replace('v', '');
const npmVersion = execSync('npm --version').toString().trim();

// Generate the content
const content = `# AUTO-GENERATED TECHNOLOGY VERSIONS
# Generated on ${new Date().toISOString()}

NODE_VERSION=${nodeVersion}
NPM_VERSION=${npmVersion}

# Core Frameworks
REACT_VERSION=${getVersionSync('react')}
REACT_DOM_VERSION=${getVersionSync('react-dom')}
REACT_ROUTER_VERSION=${getVersionSync('react-router-dom')}

# UI Libraries
TAILWINDCSS_VERSION=${getVersionSync('tailwindcss')}

# Backend Services
FIREBASE_VERSION=${getVersionSync('firebase')}

# Additional Libraries
AXIOS_VERSION=${getVersionSync('axios')}
`;

// Write to file
fs.writeFileSync(path.join(process.cwd(), '.env.versions'), content);
console.log('✅ .env.versions file generated successfully!');
console.log('Versions successfully written to .env.versions file');