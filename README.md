# TLS-comparison

This script compares most common TLS1.3 ciphers efficiency

# Results from different CPUs

This is the script output collected from various CPUs

## AES-NI enabled Intel procesor

flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx rdtscp lm constant_tsc arch_perfmon nopl xtopology tsc_reliable nonstop_tsc cpuid pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx hypervisor lahf_lm pti ssbd ibrs ibpb stibp tsc_adjust arat md_clear flush_l1d arch_capabilities
Cipher Performance Results (Min/Max/Avg Times in Seconds):

### Cipher Performance Results (Min/Max/Avg Times in Seconds)

| Cipher                      | Enc Min   | Enc Max   | Enc Avg   | Dec Min   | Dec Max   | Dec Avg   | Total Avg | Success |
|----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------|
| TLS_AES_128_GCM_SHA256     | 0.000055  | 0.000272  | 0.000059  | 0.000054  | 0.000226  | 0.000058  | 0.000117  | 1       |
| TLS_AES_256_GCM_SHA384     | 0.000061  | 0.000144  | 0.000065  | 0.000061  | 0.000156  | 0.000064  | 0.000129  | 1       |
| TLS_CHACHA20_POLY1305_SHA256 | 0.000080 | 0.000163  | 0.000084  | 0.000079  | 0.000136  | 0.000083  | 0.000167  | 1       |
| TLS_AES_128_CCM_SHA256     | 0.000104  | 0.000182  | 0.000108  | 0.000103  | 0.000163  | 0.000107  | 0.000215  | 1       |
| TLS_AES_128_CCM_8_SHA256   | 0.000104  | 0.000203  | 0.000108  | 0.000103  | 0.000989  | 0.000108  | 0.000217  | 1       |

**Fastest Cipher:** `TLS_AES_128_GCM_SHA256` (Average Total Time: **0.000117 seconds**)



## Intel procesor without AES instruction set support

flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 cx16 pcid sse4_1 sse4_2 movbe popcnt rdrand hypervisor lahf_lm abm 3dnowprefetch ibrs_enhanced fsgsbase bmi1 bmi2 invpcid rdseed clflushopt md_clear flush_l1d arch_capabilities


### Cipher Performance Results (Min/Max/Avg Times in Seconds)

| Cipher                        | Enc Min   | Enc Max   | Enc Avg   | Dec Min   | Dec Max   | Dec Avg   | Total Avg | Success |
|------------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------|
| TLS_AES_128_GCM_SHA256       | 0.000110  | 0.002151  | 0.000136  | 0.000110  | 0.002864  | 0.000133  | 0.000268  | 1       |
| TLS_AES_256_GCM_SHA384       | 0.000142  | 0.000457  | 0.000155  | 0.000142  | 0.000566  | 0.000154  | 0.000309  | 1       |
| TLS_CHACHA20_POLY1305_SHA256 | 0.000059  | 0.014035  | 0.000078  | 0.000059  | 0.000235  | 0.000063  | 0.000141  | 1       |
| TLS_AES_128_CCM_SHA256       | 0.000329  | 0.000702  | 0.000364  | 0.000328  | 0.002376  | 0.000362  | 0.000727  | 1       |
| TLS_AES_128_CCM_8_SHA256     | 0.000329  | 0.003554  | 0.000369  | 0.000328  | 0.001121  | 0.000360  | 0.000729  | 1       |

**Fastest Cipher:** `TLS_CHACHA20_POLY1305_SHA256` (Average Total Time: **0.000141 seconds**)




## ARM procesor without AES instruction set support (RPI 4)

### Cipher Performance Results (Min/Max/Avg Times in Seconds)

| Cipher                        | Enc Min   | Enc Max   | Enc Avg   | Dec Min   | Dec Max   | Dec Avg   | Total Avg | Success |
|------------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------|
| TLS_AES_128_GCM_SHA256       | 0.001213  | 0.012243  | 0.001299  | 0.001206  | 0.004034  | 0.001289  | 0.002587  | 1       |
| TLS_AES_256_GCM_SHA384       | 0.001410  | 0.005862  | 0.001497  | 0.001403  | 0.004195  | 0.001485  | 0.002981  | 1       |
| TLS_CHACHA20_POLY1305_SHA256 | 0.000272  | 0.000606  | 0.000282  | 0.000272  | 0.000419  | 0.000279  | 0.000561  | 1       |
| TLS_AES_128_CCM_SHA256       | 0.003161  | 0.004870  | 0.003279  | 0.003131  | 0.004444  | 0.003242  | 0.006520  | 1       |
| TLS_AES_128_CCM_8_SHA256     | 0.003160  | 0.003801  | 0.003272  | 0.003135  | 0.003497  | 0.003225  | 0.006497  | 1       |

**Fastest Cipher:** `TLS_CHACHA20_POLY1305_SHA256` (Average Total Time: **0.000561 seconds**)



## ARM procesor with AES instruction set support (RPI 5)

### Cipher Performance Results (Min/Max/Avg Times in Seconds)

| Cipher                        | Enc Min   | Enc Max   | Enc Avg   | Dec Min   | Dec Max   | Dec Avg   | Total Avg | Success |
|------------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------|
| TLS_AES_128_GCM_SHA256       | 0.000029  | 0.000079  | 0.000032  | 0.000029  | 0.000079  | 0.000031  | 0.000064  | 1       |
| TLS_AES_256_GCM_SHA384       | 0.000036  | 0.000044  | 0.000036  | 0.000034  | 0.000044  | 0.000035  | 0.000070  | 1       |
| TLS_CHACHA20_POLY1305_SHA256 | 0.000093  | 0.000104  | 0.000094  | 0.000093  | 0.000103  | 0.000094  | 0.000188  | 1       |
| TLS_AES_128_CCM_SHA256       | 0.000071  | 0.000091  | 0.000071  | 0.000078  | 0.000088  | 0.000079  | 0.000151  | 1       |
| TLS_AES_128_CCM_8_SHA256     | 0.000071  | 0.000141  | 0.000071  | 0.000078  | 0.000088  | 0.000079  | 0.000151  | 1       |

**Fastest Cipher:** `TLS_AES_128_GCM_SHA256` (Average Total Time: **0.000064 seconds**)


![4579b462-75bf-41a2-8f0c-7cc63777ac0b](https://github.com/user-attachments/assets/cee7caf3-3cc1-4cde-a33e-d1964c566b22)

