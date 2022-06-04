if(NOT "/home/hiroto/@home_ws/src/washi_ex/cpp/cmake-3.13.5/Tests/CMakeTests" MATCHES "^/")
  set(slash /)
endif()
set(url "file://${slash}/home/hiroto/@home_ws/src/washi_ex/cpp/cmake-3.13.5/Tests/CMakeTests/FileDownloadInput.png")
set(dir "/home/hiroto/@home_ws/src/washi_ex/cpp/cmake-3.13.5/Tests/CMakeTests/downloads")

file(DOWNLOAD
  ${url}
  ${dir}/file3.png
  TIMEOUT 2
  STATUS status
  EXPECTED_HASH SHA1=5555555555555555555555555555555555555555
  )
