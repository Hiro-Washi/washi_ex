# CMake generated Testfile for 
# Source directory: /home/hiroto/@home_ws/src/washi_ex/cpp/cmake-3.13.5/Tests/CMakeLib
# Build directory: /home/hiroto/@home_ws/src/washi_ex/cpp/cmake-3.13.5/Tests/CMakeLib
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(CMakeLib.testGeneratedFileStream "CMakeLibTests" "testGeneratedFileStream")
add_test(CMakeLib.testRST "CMakeLibTests" "testRST" "/home/hiroto/@home_ws/src/washi_ex/cpp/cmake-3.13.5/Tests/CMakeLib")
add_test(CMakeLib.testSystemTools "CMakeLibTests" "testSystemTools")
add_test(CMakeLib.testUTF8 "CMakeLibTests" "testUTF8")
add_test(CMakeLib.testXMLParser "CMakeLibTests" "testXMLParser")
add_test(CMakeLib.testXMLSafe "CMakeLibTests" "testXMLSafe")
add_test(CMakeLib.testFindPackageCommand "CMakeLibTests" "testFindPackageCommand")
add_test(CMakeLib.testUVRAII "CMakeLibTests" "testUVRAII")
subdirs("PseudoMemcheck")
