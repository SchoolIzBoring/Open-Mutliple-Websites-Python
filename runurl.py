import webbrowser
import time

# Define the URLs
urls = [
    "https://blxxdbubbleunbl0cker.elude.wiki/",
    "https://voi.starnerd.com/",
    "https://rdeco.sse.codesandbox.io/",
    "https://epikmath.net/",
    "https://erraticphysics.com/",
    "https://helpwithschool.online/",
    "https://bypasssearch.glitch.me/",
    "https://vanadiumtn.glitch.me/",
    "https://co-browsing.net/",
    "https://sites.google.com/view/squarecode",
    "https://ubg100.github.io/",
    "https://privatesurf.net/1.html",
    "https://iridium-main-1.notquitezook.repl.co/",
    "https://phantoms.gq/",
    "https://actuallyhistory.com/",
    "https://naruto.tech/settings.html",
    "https://sites.google.com/view/theonlybunker/countdown?authuser=0",
    "https://sites.google.com/view/school-tears/toolshacks/free-books?authuser=0",
    "https://www.victim.cf/",
    "https://www.overseas.ml/",
    "https://pwoxywoxy.xan.lol/e635b8657bcd4fe19211db53fc077b30*11926/_rhsDtRM://ioZHTiGCet.Z~oiG.k-p2/",
    "https://sites.google.com/view/calebpotter/home",
    "https://pwoxywoxy.xan.lol/e635b8657bcd4fe19211db53fc077b30*60408/_rhsDtRM://dcFZ4GG4xNoJ.ixJG8.62Ua/",
    "https://pwoxywoxy.xan.lol/e635b8657bcd4fe19211db53fc077b30*51611/_rhsDtRM://GTe4TF7J2-Fil.c-ye4.YpTU/",
    "https://edurelief.co/",
    "https://corrosion.pinkleafman.repl.co/",
    "https://bypasssearch.glitch.me/",
    "https://dabfloss.ga/",
    "https://clients.nelsonshack.com/",
    "https://apexhcf.xyz/",
    "https://walnut-planet-redcurrant.glitch.me/",
    "https://google-tabs.bubboalt.repl.co/",
    "https://4.interstellardev.repl.co/",
    "https://the-t-fr.com/",
    "https://nothernschools.digital/",
    "https://rh.lwaid.dev/",
    "https://nebula-production-ec4f.up.railway.app/",
    "https://integralsolver.lol/?unlock",
    "https://staarprep-tj.ml/",
    "https://a17kegher.wixsite.com/cool-games",
    "https://bigfootubg.netlify.app/",
    "https://www.utopiaworld.ink/",
    "https://sites.google.com/view/kaidens-arcade-hidden/home",
    "https://mathshard.xyz/",
    "https://curlypooch.com/",
    "https://rocks.wiki/",
    "https://schoolookup.ga/",
    "https://167.114.102.230/",
    "https://jesus.is-a.win/",
    "https://birdseeds.xyz/",
    "https://incognito.player123456789.repl.co/",
    "https://tsunami-20.player123456789.repl.co/",
    "https://amethysts.tech/",
    "https://heaven-gateway.glitch.me/",
    "https://sites.google.com/view/poggame",
    "https://anonymouss.org/",
    "https://sites.google.com/view/unbl0cked-gxmes-dad/home",
    "https://sites.google.com/bcsd.com/monster/homepage",
    "https://sites.google.com/view/lunahub",
    "https://triway.live/proxies/",
    "https://illusive.app/",
    "https://hypertabs.cc/",
    "https://actuallyspanish.com/apps",
    "https://i.triway.live/",
    "https://m.triway.live/",
    "https://eclipse-is.pretty-cool.ml/",
    "https://sites.google.com/view/artclass-site/home?authuser=0",
    "https://studenthax.com/#",
    "https://zestercentral.carrd.co/",
    "https://poets.kazwire.com/search/",
    "https://sustaining-notch-violet.glitch.me/",
    "https://rustydusty.glitch.me/",
    "https://rukusdank.glitch.me/",
    "https://resolute-oceanic-budget.glitch.me/",
    "https://renagamer101.github.io/",
    "https://hypertabs-px.up.railway.app/",
    "https://responsible-silk-celestite.glitch.me/",
    "https://rogue-app.xyz/",
    "https://www.mercuryworld.ml/",
    "https://e.petel.us/",
    "https://saturnos.chideraokwuosa5.repl.co/Apps.html",
    "https://rd.globalcentauri.tech/",
    "https://134.209.250.149/",
    "https://clients.chocolatespicacho.com/main.html",
    "https://shuttle.cf/",
    "https://schoology.lol/",
    "https://rocks.wiki/",
    "https://qghqa.xyz/",
    "https://mathpath.xyz/",
    "https://wrld.tk/",
    "https://mathplace.co/",
    "https://manualcars.net/#",
    "https://www.learnhistory.me/",
    "https://www.learn.gq/",
    "https://www.smellyfarts.tk/home",
    "https://voi.starnerd.com/",
    "https://taco.topgweb.repl.co/",
    "https://rdeco.sse.codesandbox.io",
    "https://tunnelrush.net/",
    "https://tsunami-2-0.up.railway.app/",
    "https://epikmath.net/",
    "https://luminite.stu-calebpotter.repl.co/",
    "https://luci.nya.pub/",
    "https://ubg100.github.io/",
    "https://iridium-main-1.notquitezook.repl.co/",
    "https://www.englishhelper.tech/games/",
    "https://naruto.tech/settings.html",
    "https://www.victim.cf/",
    "https://silver-proxy.ianruff22.repl.co/",
    "https://resclient.vercel.app/",
    "https://bypasssearch.glitch.me/",
    "https://axonproxy.tk/",
    "https://helpwithschool.online/",
    "https://web-production-a65c.up.railway.app/",
    "https://depl0y.glitch.me/",
    "https://rhodium.micahvasquez.repl.co/",
    "https://nbjg.ajh499.repl.co/",
    "https://school-heaven.micahvasquez.repl.co/carrot.html",
    "https://spooky.toxicrocker182.repl.co/",
    "https://googlemath.net/",
    "https://googlemath.org/",
    "https://stats.thatguy.pw/",
    "https://rocks.wiki/",
    "https://qghqa.xyz",
    "https://mathpath.xyz/",
    "https://astroub.ml/",
    "https://thebotgavemethesame.site/",
    "https://aubruh.tech/",
    "https://romanarts.wiki/",
    "https://geometric-expression.net/",
    "https://gravity-flow.org/",
    "https://inflopnito.com/",
    "https://blockingisnotallowed.cf/",
    "https://uv-radiation.info/",
    "https://quantum-mechanics.wiki/",
    "https://moist.vercel.app",
    "https://ratsonmyphone.org/",
    "https://shirt.gq/",
    "https://milklookupguide.com/",
    "https://holyspots.ml/",
    "https://reapir.net/",
    "https://terriblestories.org",
    "https://whackylightbulb.org",
    "https://privatesurf.net/",
    "https://googlecalendar.gq",
    "https://googlecalendar.cf",
    "https://r.utopiaworld.ink/",
    "https://r.utopiaunblocker.org/",
    "https://r.midnightofficial.xyz/",
    "https://direct.rammerhead.org/",
    "https://direct2.rammerhead.org/",
    "https://x-rayphysics.net/",
    "https://neathome.org/",
    "https://extendacademy.org/",
    "https://easyacademy.school/",
    "https://limitalgebra.net/",
    "https://storefacts.org/",
    "https://the-t-fr.com/",
    "https://languagetips.net/",
    "https://creativehog.com/",
    "https://manualcars.net/",
    "https://ensuremath.com/",
    "https://bhutanfacts.xyz",
    "https://rushschool.net/",
    "https://fractiontools.com/",
    "https://cattlefood.org/",
    "https://automatic-phrygian-canvas.glitch.me/",
    "https://incogg.netlify.app/",
    "https://incogwito.netlify.app/",
    "https://x-g-x.netlify.app/",
    "https://gmonx.netlify.app/",
    "https://xgxgx.netlify.app/",
    "https://xbubblesx.netlify.app/",
    "https://xgx.netlify.app/",
    "https://gxg.netlify.app/",
    "https://76.netlify.app/",
    "https://62.netlify.app/",
    "https://4f.netlify.app/",
    "https://7x.netlify.app/",
    "https://la-dance-macabre.netlify.app/",
    "https://so-many.netlify.app/",
    "https://78.netlify.app/",
    "https://656.netlify.app/",
    "https://1211.netlify.app/",
    "https://scol.netlify.app/",
    "https://safestay.netlify.app/",
    "https://plswait.netlify.app/",
    "https://wickwoll.netlify.app/",
    "https://22271.netlify.app/",
    "https://qqqqqqqqqqqqq.netlify.app/",
    "https://dabebe.netlify.app/",
    "https://moist.vercel.app/",
    "https://sofunni.herokuapp.com/",
    "https://s-u-s.xgamesx.repl.co/",
    "https://uv-radiation.info/",
    "https://thebotgavemethesame.site/",
    "https://aubruh.tech/",
    "https://w.mmsmathhelp.gq/",
    "https://mathpath.xyz/",
    "https://inflopnito.com/",
    "https://rijitschools.ga/",
    "https://deobotsweird.ga/",
    "https://deobotsmybestfriend.ga/",
    "https://r.googlemath.org/",
    "https://r.greathomeworkhelper.com/",
    "https://r.howdoyouunblockthis.site/",
    "https://r.inflopnito.com/",
    "https://r.midnightofficial.xyz/",
    "https://r.pleasedontblock.me/",
    "https://r.schoolconcerns.com/",
    "https://r.thiswasonlyadollar.xyz/",
    "https://r.utopia.education/",
    "https://r.utopiaunblocker.org/",
    "https://r.utopiaworld.ink/",
    "https://r.vyslix.com/",
    "https://ram.thefemboy.gay/",
    "https://ram.twink.bar/",
    "https://ramm.ruralanemone.tech/",
    "https://rammer.ddns.net/",
    "https://ripple.gq/",
    "https://ripplelake.netlify.app/",
    "https://rm.connectdev.org/",
    "https://rm.prysmdev.org/",
    "https://safetyonline.live/",
    "https://scholarshipprograms.xyz/#",
    "https://sciencewithfloppa.com/#",
    "https://sidthescientist.com/",
    "https://smartowls.tk/",
    "https://winterwaffles.tk/",
    "https://winterwaffles.ml/",
    "https://winterwaffles.gq/",
    "https://winterwaffles.ga/",
    "https://winterguide.org.uk/",
    "https://view.digitalfreezer.net/",
    "https://vapor.erererek.repl.co/",
    "https://utopiaworld.ink/",
    "https://utopiabeta.tk/",
    "https://utopia.education/",
    "https://unblock.2b2t-proxy.xyz/",
    "https://www.treewiki.tk/",
    "https://treatyguide.com/",
    "https://totallyscience.github.io/",
    "https://totallyscience.co/",
    "https://totallyalgebra.com/",
    "https://thisisa.webredirect.org/",
    "https://the-t-fr.com/",
    "https://telephonecreation.xyz/",
    "https://systemya.xyz/",
    "https://studymathteacher.com/",
    "https://spotsstuff.ml/",
    "https://spotsstuff.cf/",
    "https://spanishstudy.co/",
    "https://spaceproxy.ryansong1.repl.co",
    "https://thisisforschoolonlylol.tk/",
    "https://thisisforschoolonlylol.cf/",
    "https://thisisforschoolonlylol.ml/",
    "https://thankyouallfor1000members.tk/",
    "https://thankyouallfor1000members.cf/",
    "https://thankyouallfor1000members.ml/",
    "https://pewdiepieisprettydarncool.ml/",
    "https://pewdiepieisprettydarncool.tk/",
    "https://pewdiepieisprettydarncool.cf/",
    "https://pewdiepieisprettydarncool.ga/",
    "https://pewdiepieisprettydarncool.gq/",
    "https://canvasloginpowerschool.cf/",
    "https://canvasloginpowerschool.ml/",
    "https://canvasloginpowerschool.tk/",
    "https://generalmathematics.net/",
    "https://generalmathematics.ml/",
    "https://generalmathematics.gq/",
    "https://generalmathematics.cf/",
    "https://generalmathematics.tk/",
    "https://generalmathematics.ga/",
    "https://lexiapowerup.cf/",
    "https://coolmath.ga/",
    "https://basicmathqna.ga/",
    "https://holyubofficial.net/",
    "https://ycrgv.org/",
    "https://zlxrlr.org/",
    "https://ofotmdxm.org/",
    "https://uxvvykaf.org/",
    "https://zqagifq.org/",
    "https://mrbxp.org/",
    "https://dnsttkh.org/",
    "https://oqfeqv.org/",
    "https://hsdwgj.org/",
    "https://oguvod.org/",
    "https://kcps.pw/",
    "https://mathszway.com/",
    "https://thecollegeboards.org/",
    "https://privatesurf.net/",
    "https://privateedu.org.uk/",
    "https://linearstudies.com/",
    "https://icterical.com/",
    "https://bruhfinder.com",
    "https://cherrybar.org/",
    "https://yaemiko.org/",
    "https://winterguide.org.uk/",
    "https://analystinn.net/",
    "https://treatyguide.com/",
    "https://languagetips.net/",
    "https://r.studyschooltoday.eu.org/",
    "https://blackshare.me/",
    "https://schoology.lol/",
    "https://erraticphysics.com/",
    "https://weeb-central.icu/",
    "https://generalmathematics.gq/",
    "https://epicness.cf/",
    "https://emerald.topgweb.repl.co/",
    "https://w.topgweb.repl.co/",
    "https://taco.topgweb.repl.co/",
    "https://conventionalize.org/",
    "https://ensuremath.com/",
    "https://calculateddog",
    "https://incogg.netlify.app/",
    "https://incogwito.netlify.app/",
    "https://x-g-x.netlify.app/",
    "https://gmonx.netlify.app/",
    "https://xgxgx.netlify.app/",
    "https://xbubblesx.netlify.app/",
    "https://xgx.netlify.app/",
    "https://gxg.netlify.app/",
    "https://76.netlify.app/",
    "https://62.netlify.app/",
    "https://4f.netlify.app/",
    "https://7x.netlify.app/",
    "https://la-dance-macabre.netlify.app/",
    "https://so-many.netlify.app/",
    "https://78.netlify.app/",
    "https://656.netlify.app/",
    "https://1211.netlify.app/",
    "https://scol.netlify.app/",
    "https://safestay.netlify.app/",
    "https://plswait.netlify.app/",
    "https://wickwoll.netlify.app/",
    "https://22271.netlify.app/",
    "https://qqqqqqqqqqqqq.netlify.app/",
    "https://dabebe.netlify.app/",
    "https://moist.vercel.app/",
    "https://sofunni.herokuapp.com/",
    "https://s-u-s.xgamesx.repl.co/",
    "https://uv-radiation.info/",
    "https://thebotgavemethesame.site/",
    "https://aubruh.tech/",
    "https://w.mmsmathhelp.gq/",
    "https://mathpath.xyz/",
    "https://inflopnito.com/",
    "https://rijitschools.ga/",
    "https://deobotsweird.ga/",
    "https://deobotsmybestfriend.ga/",
    "https://languagetips.net/",
    "https://r.studyschooltoday.eu.org/",
    "https://blackshare.me/",
    "https://schoology.lol/",
    "https://erraticphysics.com/",
    "https://weeb-central.icu/",
    "https://generalmathematics.gq/",
    "https://epicness.cf/",
    "https://emerald.topgweb.repl.co/",
    "https://w.topgweb.repl.co/",
    "https://taco.topgweb.repl.co/",
    "https://conventionalize.org/",
    "https://ensuremath.com/",
    "https://calculateddoge.asfdlkj.repl.co/",
    "https://bruhfinder.com/",
    "https://www.smellyfarts.tk/home",
    "https://launchpadschools.xyz/#",
    "https://learn.gq",
    "https://www.learnhistory.me/",
    "https://linearstudies.com/",
    "https://ratsonmyphone.org/",
    "https://shirt.gq/",
    "https://milklookupguide.com/",
    "https://holyspots.ml/",
    "https://reapir.net/",
    "https://terriblestories.org",
    "https://whackylightbulb.org",
    "https://privatesurf.net/",
    "https://googlecalendar.gq",
    "https://googlecalendar.cf",
    "https://r.utopiaworld.ink/",
    "https://r.utopiaunblocker.org/",
    "https://r.midnightofficial.xyz/",
    "https://direct.rammerhead.org/",
    "https://direct2.rammerhead.org/",
    "https://x-rayphysics.net/",
    "https://neathome.org/",
    "https://extendacademy.org/",
    "https://easyacademy.school/",
    "https://limitalgebra.net/",
    "https://storefacts.org/",
    "https://the-t-fr.com/",
    "https://languagetips.net/",
    "https://creativehog.com/",
    "https://manualcars.net/",
    "https://ensuremath.com/",
    "https://bhutanfacts.xyz",
    "https://rushschool.net/",
    "https://fractiontools.com/",
    "https://cattlefood.org/",
    "https://notsusfrfr.ga",
    "https://topnotchedu.cf",
    "https://tomuchhomework.cf",
    "https://schoolforu.cf",
    "https://darknessmath.gq/",
    "https://Steal-life.glitch.me/search/",
    # Add more URLs here as needed
]

# Open up to 30 tabs in groups of 5
for i in range(0, len(urls), 5):
    if i >= 25:
        break

    # Process the next group of up to 5 URLs
    urls_to_open = urls[i:i+5]
    for url in urls_to_open:
        # Try to open the URL in a web browser
        try:
            webbrowser.open(url)
        except Exception as e:
            print("Error opening URL:", url)
            print("Exception:", e)
            continue

    # Wait for the tabs to finish loading
    time.sleep(5)
