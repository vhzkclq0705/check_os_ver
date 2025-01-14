import subprocess

def get_os_version_of_mac():
    # 파이썬에서 터미널 명령어를 실행하고 결과를 원하는 형태로 변경하는 함수
    def get_macro_reply(command):
        result = subprocess.run([command], shell=True, capture_output=True, text=True).stdout
        lines = result.splitlines()
        if lines:
             return lines[0].split(":")[1].strip()
        return None

    system_filter_command = "system_profiler SPSoftwareDataType | grep 'System Version'"
    kernel_filter_command = "system_profiler SPSoftwareDataType | grep 'Kernel Version'"

    system_version = get_macro_reply(system_filter_command)
    kernel_version = get_macro_reply(kernel_filter_command)

    return {
        "system_version": system_version,
        "kernel_version": kernel_version,
    }
