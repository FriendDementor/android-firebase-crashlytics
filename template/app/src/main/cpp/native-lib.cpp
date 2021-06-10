#include <jni.h>
#include <string>

extern "C" JNIEXPORT jstring JNICALL
Java_com_example_mynativeapplication_MainActivity_stringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}

int cppfunctionname()
{
    std::string *hello = nullptr;
    return hello->size();
}

bool crash()
{
    return cppfunctionname();
}

extern "C" JNIEXPORT jstring JNICALL
Java_com_example_mynativeapplication_MainActivity_anotherStringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
    if(crash())
        return env->NewStringUTF("hello->c_str()");
}