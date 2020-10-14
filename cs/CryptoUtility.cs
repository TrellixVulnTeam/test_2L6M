using System;
using System.Security.Cryptography;
using System.Text;

public sealed class CryptoUtility
{
    private const string KEY = "RwcmlVpgRwcmlVpg";
    private const string IV = "4e5Wa71fYoT7MFEX";

    private CryptoUtility()
    {
    }

    private static AesManaged CreateAesManaged()
    {
        AesManaged aes = new AesManaged();
        aes.KeySize = 256;
        aes.BlockSize = 128;
        aes.Mode = CipherMode.CBC;
        aes.IV = Encoding.UTF8.GetBytes(IV);
        aes.Key = Encoding.UTF8.GetBytes(KEY);
        aes.Padding = PaddingMode.PKCS7;
        return aes;
    }

    public static string Encrypt(string text)
    {
        AesManaged aes = CreateAesManaged();
        byte[] byteText = Encoding.UTF8.GetBytes(text);
        byte[] encryptText = aes.CreateEncryptor().TransformFinalBlock(byteText, 0, byteText.Length);
        return Convert.ToBase64String(encryptText);
    }

    public static string Decrypt(string text)
    {
        AesManaged aes = CreateAesManaged();
        byte[] src = System.Convert.FromBase64String(text);
        byte[] dest = aes.CreateDecryptor().TransformFinalBlock(src, 0, src.Length);
        return Encoding.UTF8.GetString(dest);
    }
}
