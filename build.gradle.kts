import com.pswidersk.gradle.python.uv.UvTask

plugins {
    id("com.pswidersk.python-uv-plugin") version "0.4.25"
}

tasks {

    register<UvTask>("uvInfo") {
        description = "List UV tool info"
        args = listOf("help")
    }
    val uvEnvInstall = register<UvTask>("uvEnvInstall") {
        description = "UV environment install"
        args = listOf("venv")
    }

    val uvInstall = register<UvTask>("uvInstall") {
        description = "UV tool install"
        val requirementsFile = projectDir.resolve("requirements.txt").path
        args = listOf("pip", "install", "-r", requirementsFile)
        dependsOn(uvEnvInstall)
    }

    projectDir.resolve("problems").listFiles().forEach { file ->
        register<UvTask>("run-${file.name}") {
            description = "Run Python script: ${file.name}"
            group = "algos"
            args = listOf("run", file.resolve("script.py").path)
            val input = file.resolve("input.txt")
            if (input.exists()) {
                standardInput = input.inputStream()
            }
            environment = mapOf("OUTPUT_PATH" to file.resolve("output.txt"))
            dependsOn(uvInstall)
        }
    }

}
