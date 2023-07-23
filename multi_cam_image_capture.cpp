#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <iomanip>
#include <sstream>
#include <cstdlib>

using namespace std;

ofstream fs;
string filename = "exampleOutput100.csv";
const std::string dir = "/home/pi/indrone/test5/finalc1";

string time()
{
    // Get current time
    auto currentTime = std::chrono::system_clock::now();

    // Convert time to milliseconds since epoch
    auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(currentTime.time_since_epoch());

    // Get the current time as a string with milliseconds
    std::time_t currentTimeSeconds = std::chrono::system_clock::to_time_t(currentTime);
    std::tm *timeInfo = std::localtime(&currentTimeSeconds);

    // Format the timestamp string
    std::stringstream timestamp;
    timestamp << std::put_time(timeInfo, "%H:%M.%S") << std::setfill('0') << std::setw(3) << ms.count() % 1000;

    // Return the timestamp as a string
    return timestamp.str();
}

int main()
{
    fs.open(filename);

    fs << "Start time"
       << ","
       << "end time" << std::endl;
    int a = 0;
    for (int i = 0; i < 50; i++)
    {
        if (a > 3)
        {
            a = 0;
        }
        string A = time();
        std::string i2cset_cmd = "i2cset -y 10 0x24 0x24 0x" + to_string(a)+ "2";
        std::system(i2cset_cmd.c_str());

        std::string command = "libcamera-still --immediate --width 1920 --height 1080 -e png -o " + dir + to_string(i) + ".png --mode 4056:3040";
        std::system(command.c_str());
        string B = time();

        fs << A << "," << B << std::endl;
        a++;
        
    }

    fs.close();
    return 0;
}
