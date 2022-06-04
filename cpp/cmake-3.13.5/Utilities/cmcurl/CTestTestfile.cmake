# CMake generated Testfile for 
# Source directory: /home/hiroto/@home_ws/src/washi_ex/cpp/cmake-3.13.5/Utilities/cmcurl
# Build directory: /home/hiroto/@home_ws/src/washi_ex/cpp/cmake-3.13.5/Utilities/cmcurl
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(curl "curltest" "http://open.cdash.org/user.php")
subdirs("lib")
