import com.pswidersk.gradle.python.VenvTask

plugins {
    id("com.pswidersk.python-plugin") version "2.7.2"
}

pythonPlugin {
    pythonVersion = "3.12.2"
    condaInstaller = "Miniconda3"
    condaVersion = "py312_24.1.2-0"
}

tasks {

    register<VenvTask>("condaInfo") {
        venvExec = "conda"
        args = listOf("info")
    }

    val condaInstall by registering(VenvTask::class) {
        val requirementsFile = projectDir.resolve("requirements.txt").path
        venvExec = "conda"
        args = listOf("install", "--file", requirementsFile)
        outputs.file(requirementsFile)
    }

    projectDir.resolve("problems").listFiles().forEach { file ->
        register<VenvTask>("run-${file.name}") {
            args = listOf(file.resolve("script.py").path)
            inputFile.set(file.resolve("input.txt"))
            environment = mapOf("OUTPUT_PATH" to file.resolve("output.txt"))
            dependsOn(condaInstall)
        }
    }


}
