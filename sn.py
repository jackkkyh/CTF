stri = "JmpckGnqskgqqgknjwbskkwrcvrmdrfcnpglrgle_lbrwncqcrrgleglbsqrpw,JmpckGnqskf_q`cclrfcglbsqrpw%qqr_lb_pbbskkwrcvrctcpqglacrfc/3..q*ufcl_lslilmulnpglrcprmmi_e_jjcwmdrwnc_lbqap_k`jcbgrrmk_ic_rwncqncagkcl`mmi,Grf_qqsptgtcblmrmljwdgtcaclrspgcq*dj_eyrpGt/2j]P.R{`sr_jqmrfcjc_nglrmcjcarpmlgarwncqcrrgle*pck_glglecqqclrg_jjwslaf_lecb,Gru_qnmnsj_pgqcbglrfc/74.qugrfrfcpcjc_qcmdJcrp_qcrqfccrqamlr_glgleJmpckGnqskn_qq_ecq*_lbkmpcpcaclrjwugrfbcqirmnns`jgqfgleqmdru_pcjgic?jbsqN_ecK_icpglajsbgletcpqgmlqmdJmpckGnqsk}"

for q in range(0, 46):
    print("i = ", q)
    i = q - 27
    t = ""
    for s in stri:
        t += chr(ord(s)+i)
    print(t)


