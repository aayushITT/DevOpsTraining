# Enabling Code Coverage, SAST, and DAST in Azure DevOps

## 1. Overview

In modern DevOps practices, integrating security and test coverage directly into CI/CD pipelines is crucial. Azure DevOps supports several tools and extensions that allow teams to implement:

- Code Coverage
- Static Application Security Testing (SAST)
- Dynamic Application Security Testing (DAST)

This document outlines the theory and steps to enable these practices in Azure DevOps Pipelines.

---

## 2. Code Coverage

### What is Code Coverage?

Code coverage is a software testing metric that measures the percentage of source code executed during automated testing. It helps identify untested parts of the application, guiding teams to improve test quality.

### Why It Matters

- Validates test effectiveness
- Helps ensure critical code paths are covered
- Supports continuous quality improvement

### Steps to Enable Code Coverage in Azure DevOps

1. **Add a test task to your pipeline**:
   Use the appropriate test task for your programming language (e.g., DotNetCoreCLI for .NET, Maven for Java).
   
2. **Enable code coverage collection**:
   Modify the test task to include the appropriate arguments to collect code coverage (e.g., `--collect:"Code Coverage"` for .NET).

3. **Publish code coverage results**:
   Add a `PublishCodeCoverageResults` task to publish the coverage report.

4. **Review coverage in Azure DevOps**:
   Navigate to the pipeline run and check the "Tests" tab to view code coverage metrics.

---

## 3. Static Application Security Testing (SAST)

### What is SAST?

Static Application Security Testing is the process of analyzing source code, binaries, or bytecode for vulnerabilities without executing the program. It is performed during the early stages of development, often as part of continuous integration.

### Why It Matters

- Identifies vulnerabilities early in the SDLC
- Prevents deployment of insecure code
- Supports compliance and secure coding standards

### Steps to Enable SAST in Azure DevOps (using SonarCloud)

1. **Install the SonarCloud extension**:
   Go to the Azure DevOps Marketplace and install the SonarCloud extension.

2. **Create a service connection to SonarCloud**:
   In Azure DevOps, navigate to Project Settings > Service Connections and add a SonarCloud connection.

3. **Add SonarCloud tasks to your pipeline**:
   Include the following tasks in your YAML pipeline:
   - `SonarCloudPrepare`: Configures the project and scanner.
   - `Build Task`: Compiles the project.
   - `SonarCloudAnalyze`: Runs the static analysis.
   - `SonarCloudPublish`: Publishes results to SonarCloud.

4. **View results in SonarCloud**:
   Visit your SonarCloud dashboard to view code smells, bugs, and security issues.

### Alternative SAST Tools

- CodeQL (via GitHub Actions or command line)
- Fortify, Checkmarx, or other commercial SAST tools

These may require custom script tasks or Docker integration.

---

## 4. Dynamic Application Security Testing (DAST)

### What is DAST?

Dynamic Application Security Testing analyzes a running application to identify vulnerabilities that appear during runtime. Unlike SAST, it does not require access to source code and simulates real-world attacks.

### Why It Matters

- Detects runtime vulnerabilities such as authentication issues, insecure APIs, etc.
- Complements SAST by covering runtime behavior
- Helps secure publicly accessible applications

### Steps to Enable DAST in Azure DevOps (using OWASP ZAP)

1. **Deploy your application to a test/staging environment**:
   Ensure the application is accessible via a public or internal URL.

2. **Run OWASP ZAP scan using Docker**:
   Add a script task to your pipeline to run the ZAP container and scan the target URL.

3. **Generate and store the scan report**:
   Save the ZAP output (e.g., HTML report) to a known location within the pipeline workspace.

4. **Publish the scan report as an artifact**:
   Use the `PublishBuildArtifacts` task to make the report available for download and review.

5. **Review the report**:
   Download the report from the build summary page and evaluate any identified issues.

### Alternative DAST Tools

- Burp Suite (Pro/Enterprise with automation)
- Netsparker
- Commercial DAST platforms that offer Azure DevOps integrations or REST APIs

---

## 5. Conclusion

Incorporating Code Coverage, SAST, and DAST into your Azure DevOps pipeline enhances both the quality and security of your software. These practices provide early feedback to developers, reduce technical debt, and protect against common security threats.

For full implementation, choose tools that fit your tech stack and compliance needs, and integrate them directly into your CI/CD process using Azure DevOps YAML pipelines.
