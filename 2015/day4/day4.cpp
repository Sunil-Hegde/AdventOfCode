#include <iostream>
#include <openssl/md5.h>
#include <openssl/evp.h>  // Add this line
#include <cstring>
#include <sstream>
#include <iomanip>

using namespace std;

string calculateMD5(const string& input) {
    EVP_MD_CTX *mdctx;
    const EVP_MD *md;
    unsigned char result[MD5_DIGEST_LENGTH];
    unsigned int len;

    md = EVP_md5();
    mdctx = EVP_MD_CTX_new();
    EVP_DigestInit_ex(mdctx, md, NULL);
    EVP_DigestUpdate(mdctx, input.c_str(), input.length());
    EVP_DigestFinal_ex(mdctx, result, &len);
    EVP_MD_CTX_free(mdctx);

    stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        ss << hex << setw(2) << setfill('0') << static_cast<int>(result[i]);
    }

    return ss.str();
}

int main() {
    string secretKey = "iwrupvqb";  // Replace with your actual secret key
    int number = 1;

    while (true) {
        string input = secretKey + to_string(number);
        string hash = calculateMD5(input);

        // Check if the hash starts with at least five zeroes
        if (hash.substr(0, 6) == "000000") {
            cout << "The lowest number is: " << number << endl;
            break;
        }

        number++;
    }

    return 0;
}
