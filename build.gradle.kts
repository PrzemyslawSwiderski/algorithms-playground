import com.pswidersk.gradle.python.uv.UvTask

plugins {
    id("com.pswidersk.python-uv-plugin") version "0.2.0"
}

tasks {

    register<UvTask>("uvInfo") {
        args = listOf("help")
    }

    val uvEnvInstall by registering(UvTask::class) {
        args = listOf("venv")
    }

    val uvInstall by registering(UvTask::class) {
        val requirementsFile = projectDir.resolve("requirements.txt").path
        args = listOf("pip", "install", "-r", requirementsFile)
        dependsOn(uvEnvInstall)
    }

    projectDir.resolve("problems").listFiles().forEach { file ->
        register<UvTask>("run-${file.name}") {
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
