#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cout << "Usage: .'/home/peregrine/test_red_armor.jpg' 

" <<
        return -1;
    }

    std::string img_path = argv[1];
    cv::Mat image = cv::imread(img_path);
    if (image.empty()) {
        std::cout << "Error: Could not load image." << std::endl;
        return -1;
    }

    cv::Mat hsv;
    cv::cvtColor(image, hsv, cv::COLOR_BGR2HSV);

    cv::Mat mask1, mask2, mask;
    cv::inRange(hsv, cv::Scalar(0, 100, 100), cv::Scalar(10, 255, 255), mask1);
    cv::inRange(hsv, cv::Scalar(160, 100, 100), cv::Scalar(179, 255, 255), mask2);

    cv::bitwise_or(mask1, mask2, mask);

    cv::imshow("Original Image", image);
    cv::imshow("Red Mask", mask);

    cv::waitKey(0);
    return 0;
}