# Artificial_Intelligence_MIT

                                                      CRYPTOGRAPHIC ALGORITHMS

MIT 6.034 Artificial Intelligence Projects

The 5 core principles of Cybersecurity are Confidentiality, Integrity, Availability, Authentication and Non-Repudiation. Cryptography Algorithms are the foundational core responsible for 4 of them with the exception of Availability.

The project is an extension of my Network Security and Advanced Network Security Courses, but a decoupling of my Masters Thesis in 2016 at TMU, by exploring the updated algorithms used for the Secure Enterprise Network Design project. I researched the most secured encryption algorithms currently available in 2023 which are AES-256_GCM and RSA-4096 key size (Symmetric and Asymmetric Encryption). Four of the top Secure Hashing Function Algorithms which are (sha512, sha3_384, sha3_512, blake2b). And lastly the secure key exchange algorithm from Diffie-Hellman using 4096 key size.

This was written in Python 3.xx programming language for the AI course project.
______________________________________________________________________________________________________________________________________________________

                          BUILT A 2FA/MFA (TOTP) and (HOTP) APPLICATION WITH A SECURE PASSWORD GENERATOR

A SaaS based multifactor authenticator TOTP(Time Based One Time Password) app was created using Python3.x programming language to verify users identity to an application(Privateboss_App) given integration with (Microsoft/Google) authenticator applications and QRcode download was enabled for initial identity verification.

Offline/Recovery code application was created to ensure users can still login into the application if there is no internet service or after 5 failed attempt with authenticator's One Time Password using HOTP (HMAC One Time Password)

A Secure Password Generator was also built to offer great password security. While I strongly advocate for SSO(Single Sign On) with 2FA/MFA as part of a strong identity solution, a secure random password with a minimum of 15 strings is a better alternative to reusing passwords on multiple platforms. 
